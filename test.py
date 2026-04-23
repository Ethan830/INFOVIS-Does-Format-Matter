import google.generativeai as genai
import base64

# --- CONFIGURATION ---
# Use your NEW Google AI Studio key here
GEMINI_KEY = "AIzaSyDGFBcq30pVc7vd6U-aU-jChJsdQ2wFW0Y"

# 1. Initialize the Google SDK correctly
genai.configure(api_key=GEMINI_KEY)

def call_gemini_flash_lite(prompt, content, modality):
    # Use the exact string from your pricing screenshot
    model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
    
    if modality == "rendered image":
        # Ensure 'content' is the base64 encoded string
        img_data = base64.b64decode(content)
        # Proper Gemini multimodal format
        response = model.generate_content([
            prompt, 
            {"mime_type": "image/png", "data": img_data}
        ])
    else:
        # Standard text-based call
        response = model.generate_content(f"{prompt}\n\nData:\n{content}")
        
    return response.text

# --- TEST IT ---
try:
    print("Testing connection...")
    test_response = call_gemini_flash_lite("Hello, respond with 'Success' if you can hear me.", "", "text")
    print(f"Server Response: {test_response}")
except Exception as e:
    print(f"Still getting an error: {e}")