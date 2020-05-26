class Duck:
    sound = 'Quaaaack!'
    walking = 'Walk like a duck.'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


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


def main():
    Donald = Duck()
    Donald.quack()
    Donald.walk()

    my_car = Car()
    print("I'm a car!")
    my_car.accelerate()
    my_car.say_state()


if __name__ == '__main__':
    main()
