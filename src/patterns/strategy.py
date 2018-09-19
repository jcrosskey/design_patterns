'''
Strategy pattern

Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
'''
from abc import ABC, abstractmethod


class AbsFlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        """
        fly
        """


class FlyWithWings(AbsFlyBehavior):

    def fly(self):
        print("I'm flying!")


class FlyNoWay(AbsFlyBehavior):

    def fly(self):
        print("I can't fly!")


class AbsQuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        """
        quack
        """


class Quack(AbsQuackBehavior):

    def quack(self):
        print('Quack')


class MuteQuack(AbsQuackBehavior):

    def quack(self):
        print('<< Silence >>')


class Squeak(AbsQuackBehavior):

    def quack(self):
        print('Squeak')


class AbsDuck(ABC):

    def __init__(self, fly_behavior, quack_behavior):
        assert isinstance(fly_behavior, AbsFlyBehavior)
        assert isinstance(quack_behavior, AbsQuackBehavior)
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior):
        assert isinstance(fly_behavior, AbsFlyBehavior)
        self._fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        assert isinstance(quack_behavior, AbsQuackBehavior)
        self._quack_behavior = quack_behavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def swim(self):
        print('All ducks float, even decoys!')


class MallardDuck(AbsDuck):

    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'm mallard duck")


class ModelDuck(AbsDuck):

    def __init__(self):
        super().__init__(FlyNoWay(), Quack())


class Main(object):

    def main(self):
        mallard = MallardDuck()
        mallard.display()
        mallard.perform_fly()
        mallard.perform_quack()

        model = ModelDuck()
        model.perform_fly()
        model.set_fly_behavior(FlyWithWings())
        model.perform_fly()


if __name__ == '__main__':
    Main().main()
