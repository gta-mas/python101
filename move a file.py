import os

source = "C:\\Users\\Gabo\\Desktop\\test.txt"
destination = "C:\\Users\\Gabo\\Desktop\\folder\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" was not found!")

