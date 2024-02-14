# Used to securely store your API key
# from google.colab import userdata
import google.generativeai as genai
import os

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
