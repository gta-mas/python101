# classes can inherit attributes/methods from another class
# they then form a child/parent relationship -> child receives everything the parent class has

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")


class Fish(Animal):
    def swim(self):
        print("Fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
# rabbit.run()
# fish.swim()
# hawk.fly()