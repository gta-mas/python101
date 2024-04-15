import time

# print(time.ctime(0))        # converts a time expressed in seconds since epoch to a readable string
                              # epoch = when your computer thinks time began (reference point)

# print(time.time())            # returns current seconds since epoch
#
# # print(time.ctime(time.time()))  # current date and time
# time_object = time.localtime()
# time_object = time.gmtime()       # UTC coordinated universal time
#
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y") # parses a string representation of a time/date and returns a time object

# print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)      # accepts a time object or a tuple representation of a relative time following a formula:
                                            # (year, month, day, hour, minute, second, day of the week, day of the year, dst)
print(time_string)

time_string = time.mktime(time_tuple)       # converts tuple representation of time into seconds since epoch
print(time_string)