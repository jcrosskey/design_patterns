'''
State Pattern

Allow an object to alter its behavior when its internal state changes. The object will appear (to the client)
to change its class.
Extract each logic to a separate class and let the context delegate teh behavior to the corresponding state class.

What does it mean by "appear to change its class"? From the perspective of a client, if the object you are using
completely changes its behavior, it appears to you that the object is actually instantiated from a different class.
This happens because we use composition to give the appearance of a class change by referencing different state
objects.

Components:
* Context: the object that has finite number of states
* Finite number of predefined states
* Finite number of predefined transitions between the states
* Actions that the context supports and potentially triggers transitions between states

Examples:
* A gumball machine can have states: no_quarter, has_quarter, single_gumball, double_gumball, sold_out
* A cellphne can have states: off, locked, ready
* An electric car can have states: off, climate_only, on, charging

Structure of the pattern:
* Context (object that has different states) has a state attribute of interface "State", and interact with states
via the State interface.
* State interface defines the actions the object can take, they should be common aross all concrete states.
* Concrete states implement State interface, and the action methods, potentially via the context.
* Both context and states can modify the states or perform the transitions.

Principles applied:
* Single Responsibility
* Open-Closed

Benefits:
* Avoid many if-else logic and state switching procedures
* New states can be introduced easily
'''

from abc import ABC
from abc import abstractmethod

# We will implement the gumball machine example

class AbsGBState(ABC):
    """
    Interface for gumball state.
    Defines all the actions the context/states support.
    Our gumball has these concrete states for now:
    no_quarter, has_quarter, one_ball_win, double_ball_win, sold_out.

    What are the reasonable transitions between them?
    """
    @abstractmethod
    def insert_quarter(self):
        """
        insert quarter in the machine
        """

    @abstractmethod
    def eject_quarter(self):
        """
        eject quarter from the machine
        """

    @abstractmethod
    def turn_crank(self):
        """
        turn the machine's crank
        """

    @abstractmethod
    def dispense(self):
        """
        dispense gumball
        """

# Implement these concrete states: no_quarter, has_quarter, one_ball_win, double_ball_win, sold_out.
class NoQuarterState(AbsGBState):
    def __init__(self, gb_machine):
        self.__gb_machine = gb_machine

    def insert_quarter(self):
        self.__gb_machine.set_state(self.__gb_machine.get_has_quarter_state())
        if self.__gb_machine.get_count() == 0:
            print(f'There is no gumball left in the machine!')
            self.__gb_machine.eject_quarter()

    def eject_quarter(self):
        print(f'You have not inserted a quarter')

    def turn_crank(self):
        print(f'You turned, but there is no quarter')

    def dispense(self):
        print(f'You need to pay first')

class HasQuarterState(AbsGBState):
    def __init__(self, gb_machine):
        self.__gb_machine = gb_machine

    def insert_quarter(self):
        print(f'You already inserted a quarter')

    def eject_quarter(self):
        self.__gb_machine.set_state(self.__gb_machine.get_no_quarter_state())

    def turn_crank(self):
        import numpy as np
        turned_int = np.random.randint(0, 10)
        curr_count = self.__gb_machine.get_count()
        if turned_int == 0 and curr_count > 1:
            print(f'Yay, you got a winner! Double gumball!')
            self.__gb_machine.set_state(self.__gb_machine.get_two_ball_win_state())
        else:
            assert curr_count > 0
            print(f'You won a ball!')
            self.__gb_machine.set_state(self.__gb_machine.get_one_ball_win_state())

    def dispense(self):
        print(f'You need to turn the crank first')

class OneBallWinState(AbsGBState):
    def __init__(self, gb_machine):
        self.__gb_machine = gb_machine

    def insert_quarter(self):
        print(f'You already inserted a quarter, and we are ready to dispense gumball')

    def eject_quarter(self):
        print(f'You already turned the crank, we are ready to dispense gumball, cannot eject quarter now')

    def turn_crank(self):
        print(f'You already turned the crank, we are ready to dispense gumball')

    def dispense(self):
        self.__gb_machine.release_one_ball()
        if self.__gb_machine.get_count() > 0:
            self.__gb_machine.set_state(self.__gb_machine.get_no_quarter_state())
        else:
            self.__gb_machine.set_state(self.__gb_machine.get_sold_out_state())

class TwoBallWinState(AbsGBState):
    def __init__(self, gb_machine):
        self.__gb_machine = gb_machine

    def insert_quarter(self):
        print(f'You already inserted a quarter, and we are ready to dispense gumball')

    def eject_quarter(self):
        print(f'You already turned the crank, we are ready to dispense gumball, cannot eject quarter now')

    def turn_crank(self):
        print(f'You already turned the crank, we are ready to dispense gumball')

    def dispense(self):
        self.__gb_machine.release_one_ball()
        self.__gb_machine.release_one_ball()
        if self.__gb_machine.get_count() > 0:
            self.__gb_machine.set_state(self.__gb_machine.get_no_quarter_state())
        else:
            self.__gb_machine.set_state(self.__gb_machine.get_sold_out_state())

class SoldOutState(AbsGBState):
    def __init__(self, gb_machine):
        self.__gb_machine = gb_machine

    def insert_quarter(self):
        print(f'All sold out, cannot accept quarter')

    def eject_quarter(self):
        print(f'All sold out, no quarter accepted or ejected')

    def turn_crank(self):
        print(f'All sold out, cannot turn crank')

    def dispense(self):
        print(f'All sold out')

# The context
class GumballMachine(object):
    """
    This is the "context".
    """

    def __init__(self, num_gum_ball):
        assert isinstance(num_gum_ball, int)
        self.__num_gum_ball = num_gum_ball
        self.__no_quarter_state = NoQuarterState(self)
        self.__has_quarter_state = HasQuarterState(self)
        self.__one_ball_win_state = OneBallWinState(self)
        self.__two_ball_win_state = TwoBallWinState(self)
        self.__sold_out_state = SoldOutState(self)

        self.__state = self.__no_quarter_state if self.__num_gum_ball > 0 else self.__sold_out_state

    def insert_quarter(self):
        self.__state.insert_quarter()

    def eject_quarter(self):
        self.__state.eject_quarter()

    def turn_crank(self):
        self.__state.turn_crank()
        self.__state.dispense()

    def set_state(self, gb_state):
        assert isinstance(gb_state, AbsGBState)
        self.__state = gb_state

    # methods that can be used by states
    def release_one_ball(self):
        print(f'A gumball comes rolling out of the slot...')
        if self.__num_gum_ball > 0:
            self.__num_gum_ball -= 1

    def get_count(self):
        return self.__num_gum_ball

    def get_state(self):
        return self.__state

    def get_no_quarter_state(self):
        return self.__no_quarter_state

    def get_has_quarter_state(self):
        return self.__has_quarter_state

    def get_one_ball_win_state(self):
        return self.__one_ball_win_state

    def get_two_ball_win_state(self):
        return self.__two_ball_win_state

    def get_sold_out_state(self):
        return self.__sold_out_state

    def __str__(self):
        return f'State Pattern Gumball Machine total {self.__num_gum_ball} balls left'

if __name__ == '__main__':
    """
    What if there are multiple gumball machines??

    $ python state.py 
    State Pattern Gumball Machine total 10 balls left
    You won a ball!
    A gumball comes rolling out of the slot...
    You won a ball!
    A gumball comes rolling out of the slot...
    State Pattern Gumball Machine total 8 balls left


    You won a ball!
    A gumball comes rolling out of the slot...
    You won a ball!
    A gumball comes rolling out of the slot...
    State Pattern Gumball Machine total 6 balls left


    You won a ball!
    A gumball comes rolling out of the slot...
    You won a ball!
    A gumball comes rolling out of the slot...
    State Pattern Gumball Machine total 4 balls left


    You won a ball!
    A gumball comes rolling out of the slot...
    You won a ball!
    A gumball comes rolling out of the slot...
    State Pattern Gumball Machine total 2 balls left


    Yay, you got a winner! Double gumball!
    A gumball comes rolling out of the slot...
    A gumball comes rolling out of the slot...
    All sold out, cannot accept quarter
    All sold out, cannot turn crank
    All sold out
    State Pattern Gumball Machine total 0 balls left


    All sold out, cannot accept quarter
    All sold out, cannot turn crank
    All sold out
    All sold out, cannot accept quarter
    All sold out, cannot turn crank
    All sold out
    State Pattern Gumball Machine total 0 balls left
    """
    gb = GumballMachine(10)
    print(gb)

    for i in range(6):
        gb.insert_quarter()
        gb.turn_crank()
        gb.insert_quarter()
        gb.turn_crank()

        print(gb)
        print('\n')
