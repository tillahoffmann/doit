"""extra goodies to be used in dodo files"""

import os

def create_folder(dir_path):
    """create a folder in the given path if it doesnt exist yet."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return True