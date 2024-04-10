# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept varying amount of positional arguments

# def add(*args):
#     sum = 0
#     args = list(args)         # if we want to update a tuple, need to cast it as a list then it is changeable
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))