# thread = flow of execution, like a separate order of instructions
# each thread takes a turn running to achieve concurrency
# GIL = Global Intepreter Lock, allos only one thread to hold the control of the Python interpreter at any one time
# programs/tasks can be divided into 2 categories:

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
# better to use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
# better to use multithreading
import threading
import time
start = time.perf_counter()

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_tea():
    time.sleep(4)
    print("You drank tea")


def study():
    time.sleep(5)
    print("You finished studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_tea, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# x.join()
# y.join()
# z.join()

# eat_breakfast()
# drink_tea()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start)
