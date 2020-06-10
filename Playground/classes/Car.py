class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print(f"I'm going {self.speed} kpm!")

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

    # Numeric methods

    # self + other
    def __add__(self, other):
        return Car(self.speed + other.speed)

    # self += other
    def __iadd__(self, other):
        self.speed += other.speed
        return self

    # self - other
    def __sub__(self, other):
        return Car(self.speed - other.speed)

    # self * other
    # def __mul__(self, other):
    #     pass
    # self / other
    # def __divmod__(self, other):
    #     pass
    # self // other
    # def __floordiv__(self, other):
    #     pass
    # self ** other
    # def __pow__(self, power, modulo=None):
    #     pass
    # self & other
    # def __and__(self, other):
    #     pass
    # self | other
    # def __or__(self, other):
    #     pass

    # Comparison operators
    # Note: These are also used in internal sorting functions and will change out lists of objects will be sorted

    # self > other
    # def __gt__(self, other):
    #     return self.speed > other.speed
    # self >= other
    # def __ge__(self, other):
    #     return self.speed >= other.speed
    # self < other
    # def __It__(self, other):
    #     return self.speed < other.speed
    # self <= other
    # def __le__(self, other):
    #     return self.speed <= other.speed
    # self == other
    # def __eq__(self, other):
    #     return self.speed == other.speed
    # self != other
    # def __ne__(self, other):
    #     return self.speed != other.speed

    def __repr__(self):
        return f'Car - Speed:{self.speed} Odometer:{self.odometer} Time:{self.time}'


def main():
    my_car = Car()
    print("I'm a car!")
    my_car.accelerate()
    my_car.say_state()

    # This dynamically adds a property and value to a class
    setattr(my_car, 'prop', 'Value')
    print(my_car.prop)

    prop_key = 'prop2'
    prop_value = 'Value2'
    setattr(my_car, prop_key, prop_value)

    prop2 = getattr(my_car, prop_key)
    print(prop2)

    # Usng this in a loop. Potentially useful when creating basic data objects
    car_info = {'make': 'Ford', 'name': 'Mustang'}
    for key, value in car_info.items():
        setattr(my_car, key, value)

    print(my_car.make, my_car.name)

    for key in car_info.keys():
        print(getattr(my_car, key))

    car1 = Car(100)
    car2 = Car(200)
    car1 += car2
    car3 = car1 + car2
    car4 = car3 - car1
    print(car3, car4)


if __name__ == '__main__':
    main()
