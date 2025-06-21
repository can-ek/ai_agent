import unittest

# from subdirectory.filename import function_name
from functions.run_python import run_python_file

class TestGetFilesInfo(unittest.TestCase):
  result = run_python_file("calculator", "main.py")
  print(result)
  
  result = run_python_file("calculator", "tests.py")
  print(result)

  result = run_python_file("calculator", "../main.py")
  print(result)

  result = run_python_file("calculator", "nonexistent.py")
  print(result)

if __name__ == "__main__":
    TestGetFilesInfo()