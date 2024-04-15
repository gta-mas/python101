# Higher Order Function = a function that either:
# 1. accepts a functions as an argument
# or
# 2. returns a function as output (since in Python, functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(function):
    text = function("Hello!")
    print(text)


hello(loud)
hello(quiet)


# -----------------------------------------------


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))
