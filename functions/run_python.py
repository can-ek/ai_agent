import os
import subprocess

def run_python_file(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  target_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_path.startswith(abs_working_dir):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  if not os.path.exists(target_path):
    return f'Error: File "{file_path}" not found.'
  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'
  
  try:
    proc = subprocess.run(['python3.13', target_path],  timeout=30, encoding='utf-8', text=True, capture_output=True)
    result = f'STDOUT: {proc.stdout}\nSTDERR: {proc.stderr}'
    if proc.returncode != 0:
      result = f'{result}\nProcess exited with code {proc.returncode}'
    return result
  except Exception as e:
    return f"Error: executing Python file: {e}"