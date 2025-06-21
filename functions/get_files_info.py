import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

def get_file_content(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  target_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_path.startswith(abs_working_dir):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(target_path):
      return f'Error: File not found or is not a regular file: "{file_path}"'
  
  try:
    MAX_CHARS = 10000
    file_content_string = ''

    with open(target_path, "r") as f:
      file_content_string = f.read(MAX_CHARS) 

    if os.path.getsize(target_path) > MAX_CHARS:
      file_content_string = f'{file_content_string} [...File "{file_path}" truncated at 10000 characters]'

    return file_content_string
  except Exception as e:
    return f'Error: {e}'
  
def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  target_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  try:
     with open(target_path, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
     return f'Error: {e}'