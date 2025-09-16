import os
from pathlib import Path
from functions.is_path_in_directory import is_path_in_directory
from config import MAX_READ_FILE_CHAR


def get_file_content(working_directory, file_path):

    path = os.path.join(working_directory, file_path)
    working_directory = Path(working_directory).resolve()
    path = Path(path).resolve()
    if not is_path_in_directory(working_directory, path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"' 

    try:

        with open(path, 'r') as f:
            file_content = f.read(MAX_READ_FILE_CHAR)
        

        print(f"len: {len(file_content)}")
        if len(file_content) >= MAX_READ_FILE_CHAR:
            return "".join([file_content, "\n", f"[...File \"{path}\" truncated at {MAX_READ_FILE_CHAR} characters]"])
        
        
        return file_content
    except Exception as e:
        return f"Error: {e}"
    
    