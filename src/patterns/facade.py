'''
The Facade Pattern provides a unified interface to a set of interfaces in a subsystem.
Facade defines a higher level interface that makes the subsystem easier to use.

Design Principle
Principle of Least Knowledge: talk only to your immediate friends.

Be careful of the number of classes any object interacts with and
how it comes to interact with those classes.
'''
from abc import ABC, abstractmethod


# Class that demonstrates the (4) ways you can call methods and still adhere to the Principle of Least Knowledge

class GoodCar(object):

    def __init__(self, engine):
        self.__engine = engine

    def start(self, key):
        doors = Doors()
        # call a method of an object passed in as parameter
        authorized = key.turns()
        if authorized:
            # method of a component
            self.__engine.start()
            # method of the object itself
            self.update_dash()
            # method of objects created in the local method
            doors.lock()
        # Bad
        self.get_dash().get_info_tainment().turn_on_radio()

    def update_dash(self):
        print('Dashboard is lit and displaying info!)
