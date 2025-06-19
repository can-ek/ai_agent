import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
'''
if len(sys.argv) < 2:
  print("Error: Missing prompt argument pos 1")
  exit(1)

prompt = sys.argv[1]
messages = [ types.Content(role="user", parts=[types.Part(text=prompt)]), ]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
content_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

print(content_response.text)

if "--verbose" in sys.argv:
  print(f"User prompt: {prompt}")
  print(f"Prompt tokens: {content_response.usage_metadata.prompt_token_count}")
  print(f"Response tokens: {content_response.usage_metadata.candidates_token_count}")'''

from functions.get_files_info import get_files_info

result = get_files_info("calculator", "pkg")
print(result)
