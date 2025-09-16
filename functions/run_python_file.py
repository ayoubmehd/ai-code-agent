import os
from pathlib import Path
from functions.is_path_in_directory import is_path_in_directory
import subprocess
from config import RUN_PYTHON_FILE_TIMEOUT

def run_python_file(working_directory, file_path, args=[]):
    path = os.path.join(working_directory, file_path)
    working_directory = Path(working_directory).resolve()
    path = Path(path).resolve()
    if not is_path_in_directory(working_directory, path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not path.exists():
        return f'Error: File "{file_path}" not found.'
    
    if not str(path).endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", path, *args], timeout=RUN_PYTHON_FILE_TIMEOUT, capture_output=True) 

        if result.stdout:
            return f"STDOUT: {result.stdout}"
        elif result.stderr:
            return f"STDERR: {result.stderr}, Process exited with code {result.returncode}"
        else:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
