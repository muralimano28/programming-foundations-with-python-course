import os
import re

skip_files = [".DS_Store", ".git"]
path = "/Users/muralimanohar/Workspace/learning-python/prank"

def rename_files():
    # Get list of filenames in the directory.
    filenames = os.listdir(path)

    # Loop through the names and rename files.
    for file in filenames:
        if file in skip_files:
            print("Found a file with filename " + file)
            continue
        else:
            new_name = re.sub(r'\d', r'', file)
            os.rename(path + "/" + file, path + "/" + new_name)

rename_files()
