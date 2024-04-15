# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read

# squares = []
# for i in range(1,11):
#     squares.append(i * i)
# print(squares)

squares = [i * i for i in range(1,11)]
print(squares)
# list = [expression for item in iterable]
# ----------------------------------------------------------------------
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# passed_students = list(filter(lambda x: x >= 60, students))


passed_students = [i for i in students if i >= 60]
print(passed_students)
# list = [expression for item in iterable if conditional]
# ----------------------------------------------------------------------
passed_students = [i if i >= 60 else "FAILED" for i in students ]
print(passed_students)
# list = [expression if/else for item in iterable]