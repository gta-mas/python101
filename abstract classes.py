# abstract class = template = a class which contains one or more abstract methods
# it prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class (checks and balances)

# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod               # abc = abstract base class


class Vehicle(ABC):

    @abstractmethod     # decorator, must be used within any class that is abstract
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride a motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
