'''
The Adapter Pattern

The adapter pattern converst te interface of a class into another interface
the clients expect. Adapter lets classes work together that couldn't otherwise
because of incompatible interfaces.

The intent of an Adapter Pattern is to alter the interface so that it matches one a client
is expecting. The intent of a Facade Pattern is to provide a simplified interface
to the subsystem. Comparing to the Adapter Pattern the Decorator Pattern doesn't alter the
interface but adds responsibility.
'''
from abc import ABC, abstractmethod


# The interface that the client expects, or the target interface
class Duck(ABC):

    @abstractmethod
    def quack(self):
        """ quack """

    @abstractmethod
    def fly(self):
        """ fly """


class MallardDuck(Duck):

    def quack(self):
        print('Quack')

    def fly(self):
        print('I\'m flying')


# Existing interface that is not compatible with the client's expectation
class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        """ gobble """
    @abstractmethod
    def fly(self):
        """ fly """


class WildTurkey(Turkey):
    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('I\'m flying a short distance')


# Adapter that adapts any Turkey object to Duck interface.
class TurkeyAdapter(Duck):
    # turkey is our "adaptee"
    def __init__(self, turkey):
        assert isinstance(turkey, Turkey)
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        for _ in range(5):
            self._turkey.fly()
