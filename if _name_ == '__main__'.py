# if __name__ == '__main__'

# Module can be run as a standalone program
# Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run


if __name__ == "__main__":
    print("Running this module directly")
else:
    print("Running other module indirectly")



