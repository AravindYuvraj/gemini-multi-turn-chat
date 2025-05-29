# gemini_chat.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in environment.")

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize Gemini chat model with context
model = genai.GenerativeModel("gemini-1.5-flash")

# Set up chat session with optional parameters
chat = model.start_chat(history=[])

# Optional: Set model parameters (e.g., temperature)
temperature = float(input("Enter temperature (e.g. 0.7 for balanced, 1.2 for creative): ") or "0.7")

# First input
user_input_1 = input("👤 You (1st message): ")
response_1 = chat.send_message(user_input_1, generation_config={"temperature": temperature})
print(f"Gemini (1): {response_1.text.strip()}")

# Second input
user_input_2 = input("\n👤 You (2nd message): ")
response_2 = chat.send_message(user_input_2, generation_config={"temperature": temperature})
print(f"\nGemini (2 - Final): {response_2.text.strip()}")
