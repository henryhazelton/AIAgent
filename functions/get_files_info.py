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
    
    if os.path.isfile(full_path):
        file_parts = [full_path.split()]
        file = file_parts[-1]
    
    string_ReadMe = f'- README.md: file_size={os.path.getsize(file)}, is_dir={os.path.isdir(file)}'
    string_src = f'- src: file_size={os.path.getsize(file)}, is_dir={os.path.isdir(file)}'
    string_packageJson = f'- package.json: file_size={os.path.getsize(file)}, is_dir={os.path.isdir(file)}'