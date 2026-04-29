# import google.generativeai as genai
# import base64

# # --- CONFIGURATION ---
# # Use your NEW Google AI Studio key here
# GEMINI_KEY = "AIzaSyDGFBcq30pVc7vd6U-aU-jChJsdQ2wFW0Y"

# # 1. Initialize the Google SDK correctly
# genai.configure(api_key=GEMINI_KEY)

# def call_gemini_flash_lite(prompt, content, modality):
#     # Use the exact string from your pricing screenshot
#     model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
    
#     if modality == "rendered image":
#         # Ensure 'content' is the base64 encoded string
#         img_data = base64.b64decode(content)
#         # Proper Gemini multimodal format
#         response = model.generate_content([
#             prompt, 
#             {"mime_type": "image/png", "data": img_data}
#         ])
#     else:
#         # Standard text-based call
#         response = model.generate_content(f"{prompt}\n\nData:\n{content}")
        
#     return response.text

# # --- TEST IT ---
# try:
#     print("Testing connection...")
#     test_response = call_gemini_flash_lite("Hello, respond with 'Success' if you can hear me.", "", "text")
#     print(f"Server Response: {test_response}")
# except Exception as e:
#     print(f"Still getting an error: {e}")

import pandas as pd
import base64
from anthropic import Anthropic
import json
import re
import csv

# --- CONFIG ---
CLAUDE_KEY = "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"
client = Anthropic(api_key=CLAUDE_KEY)

TARGET_ID = "2I"
TARGET_MODALITY = "rendered image"
TARGET_Q_ID = "Q2"
TARGET_PATH = "data/2 Color Map/VIS/VIS2i.png" 

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        return json.loads(match.group()) if match else None
    except: return None

# --- RUN THE PATCH ---
print(f"Patching {TARGET_ID} | {TARGET_MODALITY} | {TARGET_Q_ID} using Claude...")

# Content Setup
sys_prompt = """You are a precise data analyst. 
You are analyzing a synthetic heat map representing abstract numerical values. 
Your task is to provide an accurate description based ONLY on the visual data.
Respond strictly in a JSON format with keys: 'answer' (string) and 'confidence' (integer)."""

# 2. Add the confidence request directly to the Question
# This forces the model to evaluate the question and the confidence simultaneously.
q_text = "What is the overall spatial pattern of the intensity across this map? " \
         "After your answer, rate your confidence in your accuracy from 0-100."

# --- IMPROVED CLAUDE PATCH ---
# Use the 'system' parameter instead of putting the prompt in the 'user' block
img_base64 = encode_image(TARGET_PATH)

try:
    response = client.messages.create(
        model="claude-sonnet-4-6", # Using the widely stable 3.5 Sonnet ID
        max_tokens=4096,
        system=sys_prompt, 
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": img_base64,
                        },
                    },
                    {"type": "text", "text": q_text}
                ],
            }
        ],
    )

    print("\n--- FULL API RESPONSE ---")
    print(response) 
    print("--------------------------\n")

    # SAFER CONTENT RETRIEVAL
    if not response.content:
        print("API Error: Claude returned an empty response. Check if your API key has credits.")
        raw_text = "{}"
    else:
        raw_text = response.content[0].text
        print(f"DEBUG: Successfully received {len(raw_text)} characters.")

except Exception as e:
    print(f"API CALL FAILED: {e}")
    raw_text = "{}"

# --- SAFER PARSING ---
parsed = extract_json(raw_text)
if parsed:
    ans = parsed.get('answer', "JSON Error")
    conf = parsed.get('confidence', 0)
else:
    ans = raw_text if raw_text != "{}" else "No response"
    conf = 0

# --- THE CSV SAVE ---
new_row = [TARGET_ID, "Claude 3.5 Sonnet", TARGET_MODALITY, TARGET_Q_ID, "", conf, ans]

with open("results.csv", "a", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)
    print("Successfully appended to results.csv")