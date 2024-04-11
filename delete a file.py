import os
import shutil

path = "C:\\Users\\Gabo\\Desktop\\folder"

try:
    # os.remove(path)
    # os.rmdir(path)        # remove directory
    shutil.rmtree(path)     # removes a directory with all files within it
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Access denied!")
except OSError:
    print("Can not delete with this function!")
else:
    print(path+" was deleted")
