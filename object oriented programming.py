from car import Car

car_1 = Car("Chevrolet", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)


Car.wheels = 2
# car_2.stop()

print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)