# reduce() = applies a function to an iterable and reduces it to a single cumulative value
# performs function on first 2 elements and repeats process until 1 value remains

# reduce (function, iterable)

import functools

# letters = ["H", "E", "L", "L", "O"]     # ["H", "E", "L", "L", "O"] -> ["HE", "L", "L", "O"] ->
                                          # ["HEL", "L", "O"] -> ["HELL", "O"] -> ["HELLO"]
# word = functools.reduce(lambda x, y: x + y, letters)
# print(word)

factorial = [5, 4, 3, 2, 1]     # [5, 4, 3, 2, 1] -> [20, 3, 2, 1]
                                # -> [60, 2, 1] -> [120, 1] -> [120]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)