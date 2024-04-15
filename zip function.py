# zip(*iterable) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements from each iterable stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "admin")
login_date = ["1/1/2021", "1/2/2021", "1/3/2024"]

users = (zip(usernames, passwords, login_date))

print(type(users))

for i in users:
    print(i)

