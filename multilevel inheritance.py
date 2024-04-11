# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal eats")

class Dog(Animal):

    def barking(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive)
dog.eat()
dog.barking()