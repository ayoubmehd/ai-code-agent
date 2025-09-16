import os
from pathlib import Path

def is_path_in_directory(working_directory, directory):
    try:

        if (working_directory == directory):
            return True
        
        directory.relative_to(working_directory)
        return True
    except ValueError:
        return False

def get_files_info(working_directory, directory="."):

    target_directory = os.path.join(working_directory, directory)
    working_directory = Path(working_directory).resolve()
    target_directory = Path(target_directory).resolve()

    if not is_path_in_directory(working_directory, target_directory):
        return f'Error: Cannot list "{target_directory}" as it is outside the permitted working directory' 

    if not target_directory.is_dir():
        return f'Error: "{target_directory}" is not a directory'
    
    try:

        stats = [f" - {item.name}: file_size={item.stat().st_size} bytes, is_dir={item.is_dir()}" for item in target_directory.iterdir()]

        return "\n".join(stats)

    except Exception as e:
        return f"Error: {e}"
    