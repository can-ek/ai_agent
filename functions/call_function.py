from get_file_content import get_file_content
from get_files_info import get_files_info
from run_python_file import run_python_file
from write_file import write_file
from google.genai import types


name_to_function = {
  'get_file_content': get_file_content,
  'get_files_info': get_files_info,
  'run_python_file': run_python_file,
  'write_file': write_file
}


def call_function(function_call_part, verbose=False):
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_call_part.name}")

  function_call_part.args['working_directory'] = './calculator'
  function_name = function_call_part.name

  if function_call_part.name not in name_to_function:
    return types.Content(
      role="tool",
      parts=[
        types.Part.from_function_response(
          name=function_name,
          response={"error": f"Unknown function: {function_name}"},
        )
      ],
    )
  
  result = name_to_function[function_name](**function_call_part.args)
  return types.Content(
    role="tool",
    parts=[
      types.Part.from_function_response(
        name=function_name,
        response={"result": result},
      )
    ],
  )