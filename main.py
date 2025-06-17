import os
import sys
from dotenv import load_dotenv
from google import genai

if len(sys.argv) != 2:
  print("Error: Missing prompt argument pos 1")
  exit(1)

prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
content_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

print(content_response.text)
print(f"Prompt tokens: {content_response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {content_response.usage_metadata.candidates_token_count}")