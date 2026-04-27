import pandas as pd
import json
import base64
import re
import time
import google.generativeai as genai
import os 
from anthropic import Anthropic
from openai import OpenAI

from question import QUESTIONS
from data.par import PAR

# --- 1. API CONFIGURATION (2026 STANDARDS) ---
# Hardcode keys or use os.environ.get("KEY_NAME")
OPENAI_KEY = "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"
CLAUDE_KEY = "YOUR_CLAUDE_KEY"
GEMINI_KEY = "AIzaSyDGFBcq30pVc7vd6U-aU-jChJsdQ2wFW0Y"

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) #OpenAI(api_key=OPENAI_KEY) replaced
anthropic_client = Anthropic(api_key=CLAUDE_KEY)
genai.configure(api_key=GEMINI_KEY)

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(f"Model Name: {m.name}")

# --- 3. PROMPT TEMPLATES ---
SYSTEM_PROMPT_TEMPLATE = """You are being shown a {modality}  representing continuous data that has been fabricated.
Answer the following question based only on the information presented. Do not use any outside knowledge.
After your answer, rate your confidence that your answer is correct as a percentage from 0% to 100%,
where 0% means you are completely guessing and 100% means you are completely certain. Use intermediate values to express partial confidence. 
Format your response as a JSON object with keys: 'answer' (string) and 'confidence' (integer)."""

# --- 4. UTILITY & API WRAPPERS ---

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return json.loads(match.group()) if match else None
    except:
        return None

#def call_gpt_5_4(prompt, content, modality): replaced with following
    #messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
    #if modality == "rendered image":
        #messages[0]["content"].append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{content}"}})
    #else:
        #messages[0]["content"][0]["text"] += f"\n\nData:\n{content}"
    #response = openai_client.chat.completions.create(model="gpt-5.4", messages=messages, response_format={"type": "json_object"})
    #return response.choices[0].message.content
def call_gpt_5_4(prompt, content, modality, model="gpt-5.4"):
    if modality == "rendered image":
        response = openai_client.responses.create(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{content}",
                        },
                    ],
                }
            ],
            text={"format": {"type": "json_object"}},
        )
    else:
        response = openai_client.responses.create(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": f"{prompt}\n\nData:\n{content}",
                        }
                    ],
                }
            ],
            text={"format": {"type": "json_object"}},
        )

    return response.output_text

def call_claude_opus_4_7(prompt, content, modality):
    msg_content = [{"type": "text", "text": prompt}]
    if modality == "rendered image":
        msg_content.append({"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": content}})
    else:
        msg_content[0]["text"] += f"\n\nData:\n{content}"
    response = anthropic_client.messages.create(model="claude-4-7-opus-20260416", max_tokens=2048, messages=[{"role": "user", "content": msg_content}])
    return response.content[0].text

def call_gemini_flash_lite(prompt, content, modality):
    model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
    
    if modality == "rendered image":
        img_data = base64.b64decode(content)
        response = model.generate_content([
            prompt, 
            {"mime_type": "image/png", "data": img_data}
        ])
    else:
        response = model.generate_content(f"{prompt}\n\nData:\n{content}")
    return response.text

# --- 5. JUDGING & SCORING FUNCTIONS ---

def judge_accuracy(model_answer, ground_truth):
    judge_prompt = f"""
    Compare the 'Model Answer' to the 'Ground Truth'. 
    If the Model Answer is factually correct (allowing for minor wording differences), output '1'.
    If the Model Answer is factually incorrect, incomplete, or contradicts the truth, output '0'.
    Ground Truth: {ground_truth}
    Model Answer: {model_answer}
    Result (0 or 1):"""
    
    # CHANGE THIS LINE to use Gemini
    raw_score = call_gemini_flash_lite(judge_prompt, "Grading Session", "text")
    return 1 if "1" in raw_score else 0

# --- 6. EXECUTION LOOP ---

results_log = []

# Mapping ID prefix to full folder name
FOLDER_MAP = {
    "1": "1 Line Graph",
    "2": "2 Color Map",
    "3": "3 Isoline",
    "4": "4 Glyph"
}

for ds in QUESTIONS:
    group_num = ds['id'][0]  # '1', '2', '3', or '4'
    folder_name = FOLDER_MAP.get(group_num)
    file_id = ds['id']       # '1A', '1B', etc. (Keeping uppercase for new files)

    # Updated paths based on your VS Code sidebar:
    # data / [Folder Name] / [MODALITY_SUBFOLDER] / [MODALITY_PREFIX][ID].[EXT]
    modality_files = {
        "rendered image": f"data/{folder_name}/VIS/VIS{file_id}.png",
        "data table": f"data/{folder_name}/DAT/DAT{file_id}.csv"
    }

    for mod_name in ["rendered image", "data table", "paragraph"]:
        try:
            if mod_name == "rendered image":
                content_to_send = encode_image(modality_files[mod_name])
            elif mod_name == "data table":
                with open(modality_files[mod_name], 'r', encoding='utf-8') as f:
                    content_to_send = f.read()
            elif mod_name == "paragraph":
                # Assuming you are still using the PAR dictionary import
                content_to_send = PAR.get(ds['id'], "Paragraph content missing.")
                
        except FileNotFoundError:
            # Helpful debug message to see exactly where it's looking
            print(f"Skipping: File not found at {modality_files.get(mod_name)}")
            continue

        for q_id, q_text in ds["questions"]:
            models = {
                "GPT-5.4": lambda prompt, content, modality: call_openai_model(
                    prompt, content, modality, model="gpt-5.4"
                ),
                # "Claude Opus 4.7": call_claude_opus_4_7,
                "Gemini 3.1 Flash Lite": call_gemini_flash_lite
            }
            for llm_name, api_func in models.items():
                print(f"Running: {llm_name} | Dataset {ds['id']} | {mod_name} | {q_id}")
                
                try:
                    # 1. Prompt LLM
                    sys_prompt = SYSTEM_PROMPT_TEMPLATE.format(modality=ds['type'])
                    full_query = f"{sys_prompt}\n\nQuestion: {q_text}"
                    raw_response = api_func(full_query, content_to_send, mod_name)
                    
                    # MANDATORY DELAY #1: Stay under 15 RPM
                    time.sleep(5) 

                    # 2. Extract & Judge
                    parsed = extract_json(raw_response)
                    ans = parsed.get('answer', raw_response) if parsed else raw_response
                    conf = parsed.get('confidence', 0) if parsed else 0
                    
                    truth = ds["ground_truth"][q_id]
                    is_correct = judge_accuracy(ans, truth)

                    # MANDATORY DELAY #2: Judge call counts toward quota too
                    time.sleep(5) 
                    
                    # 3. Log results...
                    results_log.append({
                        "Dataset_ID": ds["id"],
                        "LLM": llm_name,
                        "Modality": mod_name,
                        "Question_ID": q_id,
                        "Accuracy": is_correct,
                        "Confidence": conf,
                        "Raw_Answer": ans
                    })
                    
                except Exception as e:
                    if "429" in str(e):
                        print("Rate limit hit! Cooling down for 60 seconds...")
                        time.sleep(60) # Full reset if we hit the wall
                    else:
                        print(f"Failure on {llm_name}: {str(e)}")

# --- 7. POST-PROCESSING & ANALYSIS ---

df = pd.DataFrame(results_log)

# Calculate Brier Score: (Probability - Outcome)^2
# Probability is Confidence/100 (0.0 to 1.0)
# Outcome is Accuracy (0 or 1)
df['Brier_Score'] = ((df['Confidence'] / 100) - df['Accuracy'])**2

# Calculate ECR (Error Claim Rejection) Rate
# Only for the questions that start with 'ECR'
df['Is_ECR'] = df['Question_ID'].str.startswith('ECR')

# Save to CSV for your paper
df.to_csv("results.csv", index=False)

# Final Summary Printout
print("\n--- EXPERIMENT SUMMARY ---")
summary = df.groupby(['Modality', 'LLM']).agg({
    'Accuracy': 'mean',
    'Confidence': 'mean',
    'Brier_Score': 'mean'
}).reset_index()

print(summary)
