# str.format() = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))                                   # {} = format fields, act as a placeholder for a value or a variable, they work in order
# print("The {1} jumped over the {1}".format(animal, item))                                 # using positional argument
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))          # keyword argument

# text = "The {} jumped over the {}"

# print(text.format(animal, item))  # cleaner method
# ============================================================================
# name = "Bro"
#
# print("Hello, my name is {}.".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))     # added padding to the value, to add a positional/keyword argument, put it before the colon
# print("Hello, my name is {:<10}. Nice to meet you".format(name))    # < left align
# print("Hello, my name is {:>10}. Nice to meet you".format(name))    # > right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name))    # ^ center align
# ============================================================================
# number = 1000
#
# print("The number pi is {:.2f}".format(number))     # displays the first 2 digits after the decimal point ("f" is used in float numbers)
# print("The number is {:,}".format(number))          # separates thousands with a comma
# print("The number is {:b}".format(number))          # displays the number as binary
# print("The number is {:o}".format(number))          # displays the number as octal
# print("The number is {:x}".format(number))          # displays the number as hexadecimal
# print("The number is {:e}".format(number))          # displays the number in scientific notation










