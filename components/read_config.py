from os import path

def read_config_file(file_path):
    """
    Read and return the contents of a configuration file.

    Args:
        file_path (str): The path to the configuration file.

    Returns:
        str: The contents of the configuration file as a string.
    """
    # check if file exists
    if not path.exists(file_path):
            return ""

    with open(file_path, 'r') as file:  # Open the file in read mode
        return file.read()  # Read and return the file content as a string
