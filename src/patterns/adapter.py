'''
The Adapter Pattern

The adapter pattern converst te interface of a class into another interface
the clients expect. Adapter lets classes work together that couldn't otherwise
because of incompatible interfaces.

The Facade Pattern provides a unified interface to a set of interfaces in a subsystem.
Facade defines a higher level interface that makes the subsystem easier to use.

The intent of an Adapter Pattern is to alter the interface so that it matches one a client
is expecting. The intent of a Facade Pattern is to provide a simplified interface
to the subsystem. Comparing to the Adapter Pattern the Decorator Pattern doesn't alter the
interface but adds responsibility.

Design Principle
Principle of Least Knowledge: talk only to your immediate friends.

Be careful of the number of classes any object interacts with and
how it comes to interact with those classes.
'''
from abc import ABC, abstractmethod


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


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        assert isinstance(turkey, Turkey)
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        for _ in range(5):
            self._turkey.fly()
