# scope = the region that a variable is recognized
# a variable is only available from inside the region it is created
# a global and locally scoped version of variable can be created
# Python follows a LEGB rule = Local Enclosing Global Built-in (starts from local variable all the way to built-in)

name = "Bro"            # global variable -> global scope (available inside & outside functions)


def display_name():
    name = "Code"       # local variable -> local scope (available only inside this function)
    print(name)


display_name()
print(name)
