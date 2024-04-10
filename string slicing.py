# slicing = creating a substring by extracting elements from another string
# we can use indexing operator [] or by slice function to create a slice object ()
# 3 optional arguments [start:stop:step] starting index is inclusive, stopping index is exclusive (+1 always)
# same 3 arguments for slicing (start,stop,step)

# name = "Bro Code"
#
# first_name = name[0:3] # can leave start index blank = automatically slices from the first character
# last_name = name[4:8] # can leave the stop index blank = slices from the start index to the last character
# funky_name = name[0:8:2]
# reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 =  "http://wikipedia.com"
#
# slice = slice(7,-4)
#
# print(website1[slice])
# print(website2[slice])