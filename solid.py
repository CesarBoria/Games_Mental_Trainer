from abc import ABC, abstractmethod


class Vehicle(ABC):
    engine = True
    wheel_num: int
    vehicles_awareness = []

    def __init__(self, wheels, speed):
        self.wheels = wheels
        self.speed = speed
        self.vehicles_awareness.append(str(self))

    @abstractmethod
    def move(self):
        ...

    def __str__(self):
        return f"{__class__.__name__}"


class Wheel:
    wheels_awareness = []

    def __init__(self, diameter):
        self.diameter = diameter
        self.wheels_awareness.append(str(self))

    def __str__(self):
        return f'My diameter is {self.diameter}!'


class Car(Vehicle):
    wheel_num = 4
    wheel = Wheel(30)

    def move(self):
        print(f'I move with my {self.wheel_num} wheels of {self.wheel} cm of diameter!')

    def fuckability(self):
        print(f'Couples can fuck here, especially thanks to my big wheels! ({self.wheel}cm.)')


class Motorcycle(Vehicle):
    wheel_num = 2
    wheel = Wheel(20)

    def move(self):
        print(f'I move with my {self.wheel_num} wheels of {self.wheel} cm of diameter and feel air in my face!')

    @staticmethod
    def pass_by():
        print('I pass cars when there is traffic!')


class Uber(Car):
    @staticmethod
    def transport():
        print('I transport people')


if __name__ == '__main__':
    my_uber = Uber(30, 100)
    my_moto = Motorcycle(20, 150)
    my_moto.move()
    my_uber.move()
    my_uber.fuckability()
    my_uber.transport()
    my_moto.pass_by()
    print(my_uber.wheel.wheels_awareness)
    print(Wheel.wheels_awareness)
    print(my_uber.vehicles_awareness)
    print(Vehicle.vehicles_awareness)
