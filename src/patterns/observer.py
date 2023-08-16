"""
Observer Pattern

Defines a one-to-many dependency between objects so that when one object (subject) changes state,
all of its dependents (observers) are notified and updated automatically.

Publishers + Subscribers = Observer Pattern
"""

from abc import ABC
from abc import abstractmethod

class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        """
        """

    @abstractmethod
    def remove_observer(self, observer):
        """
        """

    @abstractmethod
    def notify_observers(self):
        """
        """

class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        """
        """


class AbsDisplay(Observer, ABC):
    @abstractmethod
    def display(self):
        """
        """

class WeatherData(Subject):

    def __init__(self, temperature=0, humidity=0, pressure=0):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.__observers = list()

    def get_temp(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_pressure(self):
        return self.__pressure

    def register_observer(self, obs):
        self.__observers.append(obs)

    def remove_observer(self, obs):
        assert obs in self.__observers
        self.__observers.remove(obs)

    def notify_observers(self):
        for obs in self.__observers:
            obs.update(self)

    def set_measurements(self, temp, humidity, pressure):
        self.__temperature = temp
        self.__humidity = humidity
        self.__pressure = pressure
        self.notify_observers()


class CurrentCondDisplay(AbsDisplay):

    def __init__(self, temperature=0, humidity=0):
        self.__temperature = temperature
        self.__humidity = humidity

    def update(self, subject):
        # Note here this class only PULLS temperature and humidity
        # How to do a PUSH method instead?
        self.__temperature = subject.get_temp()
        self.__humidity = subject.get_humidity()
        self.display()

    def display(self):
        print(f'Current conditions: {self.__temperature} F degrees, and {self.__humidity:.0f}% humidity')


class Main(object):
    """
    $ python src/patterns/observer.py
    Current conditions: 80 F degrees, and 65% humidity
    Current conditions: 82 F degrees, and 70% humidity
    Current conditions: 78 F degrees, and 90% humidity
    """

    def main(self):
        weather_data = WeatherData()
        curr_cond_display = CurrentCondDisplay()
        # OR: Let CurrentCondDisplay class HAVE WeatherData object, and register itself upon instantiation.
        weather_data.register_observer(curr_cond_display)
        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)


if __name__ == '__main__':
    Main().main()
