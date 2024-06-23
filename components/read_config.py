
# this function will read the whole text from the given config file
def read_config_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
