# method overriding = allows a sub-class (child class) to provide
# a specific implementation of a method that is already provided of one of its parents

class Animal:

    def eat(self):      # eat(self) = method signature
        print("This animal is eating")


class Rabbit(Animal):

    def eat(self):      # overrides a parent method
        print("This animal is eating a carrot")


rabbit = Rabbit()
rabbit.eat()