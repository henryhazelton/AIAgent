import os

def get_files_info(working_directory, directory="."):
    # Find absolute path of working directory
    absolute_path_working_directory = os.path.abspath(working_directory)

    # Find absolute path of target directory
    absolute_path_target_directory = os.path.abspath(os.path.join(working_directory, directory))
    
    # Validate if full path is within the working directory boundaries
    if os.path.commonpath([absolute_path_working_directory, absolute_path_target_directory]) != absolute_path_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(absolute_path_target_directory) == False:
        return f'Error: "{directory}" is not a directory'

    try: 
        contents_of_directory = os.listdir(absolute_path_target_directory)
        list_of_contents_of_directory = []

        for item in contents_of_directory:
            # Append the item name to end of target path for full path of item in directory
            full_path = os.path.join(absolute_path_target_directory, item)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path)
            string_info = f"- {item}: file_size={size} bytes, is_dir={is_dir}"
            list_of_contents_of_directory.append(string_info)
        return "\n".join(list_of_contents_of_directory)
    except Exception as e:
        return f"Error: {e}"