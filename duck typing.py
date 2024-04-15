# duck typing =  concept where the class of an object is less important that the methods/attributes that that class might have
# class type is not checked if the minimum methods/attributes are present

# "If it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck):          # chickens can both walk and talk like ducks, they can be substitute for the "duck" method
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)