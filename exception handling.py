# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:      # specific exception must be chosen, "as e" = a standard if we want to print the exception message
    print(e)
    print("You can not divide by 0!")
except ValueError as e:
    print(e)
    print("Only numbers are valid!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:            # executes this block of code, exceptions not withstanding
    print("This will always execute")











