"""
Decorator Pattern

Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing
for extending functionality.

Decorator objects can be thought of as "wrappers". They implement the same interface or abstract class as the component
they are going to decorate/wrap. It both HAS A component with the interface, but also IS A component of the same
interface.

The decorator adds its own behavior either before and/or after delegating to the object it decorates to do the rest of
the job.

Downside: add a lot of small classes to a design, making it harder for others to understand.
"""

from abc import ABC
from abc import abstractmethod

class AbsBeverage(ABC):
    """
    Interface for all beverage.
    """

    @abstractmethod
    def get_description(self):
        """
        Returns
        -------
        str
            Description of the beverage.
        """

    @abstractmethod
    def get_cost(self):
        """
        Returns
        -------
        float
            Cost of the beverage.
        """

    def __str__(self):
        return f'{self.get_description()}\t${self.get_cost():.2f}'


class AbsCondimentDecorator(AbsBeverage, ABC):
    """
    Interface for all condiment decorator.
    """

    def __init__(self, bev):
        assert isinstance(bev, AbsBeverage)
        self.__bev = bev

    def get_bev(self):
        return self.__bev


class Espresso(AbsBeverage):

    def get_description(self):
        return "espresso"

    def get_cost(self):
        return 1.99


class HouseBlend(AbsBeverage):

    def get_description(self):
        return "house blend"

    def get_cost(self):
        return 0.89


class Decaf(AbsBeverage):

    def get_description(self):
        return "decaf"

    def get_cost(self):
        return 1.05


class Mocha(AbsCondimentDecorator):
    def get_description(self):
        return f'{self.get_bev().get_description()}, Mocha'

    def get_cost(self):
        return self.get_bev().get_cost() + 0.20


class Whip(AbsCondimentDecorator):
    def get_description(self):
        return f'{self.get_bev().get_description()}, Whip'

    def get_cost(self):
        return self.get_bev().get_cost() + 0.10


class Condiment(AbsCondimentDecorator):
    """
    A generic Condiment class.
    We can have Mocha and Whip inherit this class. What's the problem with it?
    """
    def __init__(self, bev, suffix, cost):
        super().__init__(bev)
        self.__suffix = suffix
        self.__cost = cost

    def get_description(self):
        return f'{self.get_bev().get_description()}, {self.__suffix}'

    def get_cost(self):
        return self.get_bev().get_cost() + self.__cost


# What if now Beverage also has "size", and condiment price is a function of size?
class Main(object):
    """
    $ python src/patterns/decorator.py
    espresso        $1.99
    house blend, Mocha, Whip, Mocha $1.39
    decaf, Mocha, Soy, Whip $1.50
    """

    def main(self):
        bev1 = Espresso()
        print(bev1)
        bev2 = Mocha(Whip(Mocha(HouseBlend())))
        print(bev2)
        bev3 = Whip(Condiment(Mocha(Decaf()), 'Soy', 0.15))
        print(bev3)


if __name__ == '__main__':
    Main().main()
