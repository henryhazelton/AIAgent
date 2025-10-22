import os

def write_file(working_directory, file_path, content):
    
    # Find absolute path of current working directory
    absolute_path_working_directory = os.path.abspath(working_directory)

    # Find absolute path of target directory/file
    absolute_file_path= os.path.abspath(os.path.join(working_directory, file_path))
    
    # Validate if full path is within the working directory boundaries
    if os.path.commonpath([absolute_path_working_directory, absolute_file_path]) != absolute_path_working_directory:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    

    try:
        # Validate if file path exists
        if not os.path.exists(absolute_file_path):
            file_path = os.makedirs(os.path.dirname(file_path))

        # Write content to file
        with open(file_path, "w") as f:
            file_content_string = f.write(content)
            return file_content_string, f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

    except Exception as e:
        return f"Error: {e}"
    
    
