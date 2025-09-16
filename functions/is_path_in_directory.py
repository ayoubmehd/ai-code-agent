
def is_path_in_directory(working_directory, directory):
    try:

        if (working_directory == directory):
            return True
        
        directory.relative_to(working_directory)
        return True
    except ValueError:
        return False