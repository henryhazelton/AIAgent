import os

def write_file(working_directory, file_path, content):
    
    # Find absolute path of current working directory
    path_working_directory = os.path.abspath(working_directory)

    # Find absolute path of target directory/file
    file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Validate if full path is within the working directory boundaries
    if os.path.commonpath([path_working_directory, file_path]) != path_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
    # Validate if file path exists
        parent_path = os.path.dirname(file_path)
        if parent_path:
            os.makedirs(parent_path, exist_ok=True)
    
        # Write content to file
        with open(file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
    
