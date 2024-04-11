
try:
    with open("C:\\Users\\Gabo\\Desktop\\text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")


