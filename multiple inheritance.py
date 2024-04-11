# multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal hunts")


class Rabbit(Prey):
    def run(self):
        print("Rabbit is running")


class Fish(Prey, Predator):
    def swim(self):
        print("Fish is swimming")


class Hawk(Predator):
    def fly(self):
        print("Hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()