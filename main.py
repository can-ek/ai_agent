import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) < 2:
  print("Error: Missing prompt argument pos 1")
  exit(1)

schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
      ),
    },
  ),
)

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="Gets the contents of a specific file, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path to the file which contents we want to read, relative to the working directory.",
      ),
    },
  ),
)

schema_run_python_file= types.FunctionDeclaration(
  name="run_python_file",
  description="Executes a specific python file, constrained to the working directory",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path to the python file which we want to run, relative to the working directory.",
      ),
    }    
  )
)

schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="Modifies the contents of a specific file, constrained to the working directory",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path to the file which we want to write contents to, relative to the working directory.",
      ),
      "content": types.Schema(
        type=types.Type.STRING,
        description="The contents to write to the file"
      )
    }    
  )
)

available_functions = types.Tool(
  function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file
  ]
)

prompt = sys.argv[1]
messages = [ types.Content(role="user", parts=[types.Part(text=prompt)]), ]
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Run python files
- Write files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
content_response = client.models.generate_content(
  model="gemini-2.0-flash-001",
  contents=messages,
  config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

if content_response.function_calls:
  for f_call in content_response.function_calls:
    print(f"Calling function: {f_call.name}({f_call.args})")
else:
  print(content_response.text)

if "--verbose" in sys.argv:
  print(f"User prompt: {prompt}")
  print(f"Prompt tokens: {content_response.usage_metadata.prompt_token_count}")
  print(f"Response tokens: {content_response.usage_metadata.candidates_token_count}")