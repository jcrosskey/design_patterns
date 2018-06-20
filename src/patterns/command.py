'''
Created on Jun 7, 2018

From the book:

The Command Pattern encapsulates a request as an object, thereby letting you
parameterize other objects with different requests, queue or log requests,
and support undoable operations.

A command object encapsulates a request by binding together a set of actions on
a specific receiver.

The meta command pattern allows one to create macros of commands so that one can
execute multiple commands at once.

In addition to `execute` and `undo`, commands may also be used to implement logging
and transactional systems. This can by done by add methods such as `log`, `store`, `load`.
'''
from abc import ABC, abstractmethod
import sys


class Light(object):
    """ A receiver """

    def __init__(self, location=''):
        assert isinstance(location, str)
        self._location = location

    def on(self):
        print(f'{self._location} Light is on')

    def off(self):
        print(f'{self._location} Light is off')


class GarageDoor(object):

    def __init__(self, light):
        assert isinstance(light, Light)
        self._light = light

    def up(self):
        print('Garage door is open')

    def down(self):
        print('Garage door is closed')

    def stop(self):
        print('Garage door is stopped')

    def light_on(self):
        self._light.on()

    def light_off(self):
        self._light.off()


class AbsCommand(ABC):
    """
    An interface to "command" that provides one method 'execute',
    which encapsulates the actions and can be called to invoke the actions on
    the Receiver.
    """

    @abstractmethod
    def execute(self):
        """
        Execution
        """

    @abstractmethod
    def undo(self):
        """
        Undo the execution
        """


class NoCommand(AbsCommand):
    """ A null command """

    def execute(self):
        pass

    def undo(self):
        pass


class AbsLightCommand(AbsCommand, ABC):
    def __init__(self, light):
        assert isinstance(light, Light)
        self._light = light

    def set_light(self, light):
        assert isinstance(light, Light)
        self._light = light


class LightOnCommand(AbsLightCommand):

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(AbsLightCommand):

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class AbsGarageDoorCommand(AbsCommand, ABC):
    """ A concrete command """

    def __init__(self, garage_door):
        assert isinstance(garage_door, GarageDoor)
        self._garage_door = garage_door

    def set_garage_door(self, garage_door):
        assert isinstance(garage_door, GarageDoor)
        self._garage_door = garage_door


class GarageDoorOpenCommand(AbsGarageDoorCommand):
    """ A concrete command """

    def execute(self):
        self._garage_door.up()
        self._garage_door.light_on()

    def undo(self):
        self._garage_door.light_off()
        self._garage_door.down()


class GarageDoorCloseCommand(AbsGarageDoorCommand):
    """ A concrete command """

    def execute(self):
        self._garage_door.light_off()
        self._garage_door.down()

    def undo(self):
        self._garage_door.up()
        self._garage_door.light_on()


class MacroCommand(AbsCommand):
    def __init__(self, command_list=None):
        if command_list is None:
            command_list = []
        assert isinstance(command_list, list)
        for command in command_list:
            assert isinstance(command, AbsCommand)
        self._command_list = command_list

    def execute(self):
        for command in self._command_list:
            command.execute()

    def undo(self):
        for command in self._command_list[::-1]:
            command.undo()


class SimpleRemoteControl(object):
    """ Invoker
    This simple remote only has 1 button.
    Multiple slots and buttons can be added to make the remote control more complicated.
    """

    def __init__(self, command=None):
        if command is not None:
            assert isinstance(command, AbsCommand)
        self._command = command

    def set_command(self, command):
        assert isinstance(command, AbsCommand)
        self._command = command

    def button_was_pressed(self):
        self._command.execute()


class RemoteControlWithUndo(object):
    def __init__(self, num_slots):
        assert isinstance(num_slots, int)
        no_command = NoCommand()
        self._undo_command = no_command
        self._on_commands = list()
        self._off_commands = list()

        for _ in range(num_slots):
            self._on_commands.append(no_command)
            self._off_commands.append(no_command)
        self._num_slots = num_slots

    def set_command(self, slot, on_command, off_command):
        assert isinstance(slot, int)
        assert slot < self._num_slots
        assert isinstance(on_command, AbsCommand)
        assert isinstance(off_command, AbsCommand)
        print(f'Set commands for slot number {slot}')
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        assert isinstance(slot, int)
        assert slot < self._num_slots
        print(f'On button at slot number {slot} was pushed')
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_was_pushed(self, slot):
        assert isinstance(slot, int)
        assert slot < self._num_slots
        print(f'Off button at slot number {slot} was pushed')
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_was_pushed(self):
        print('Undo button was pushed')
        self._undo_command.undo()


def main():
    print('Testing simple remote control')
    remote = SimpleRemoteControl()
    light = Light()
    light_on_command = LightOnCommand(light)
    remote.set_command(light_on_command)
    remote.button_was_pressed()

    garage_door_open_command = GarageDoorOpenCommand(GarageDoor(Light('Garage')))
    remote.set_command(garage_door_open_command)
    remote.button_was_pressed()

    get_home_command = MacroCommand([light_on_command, garage_door_open_command])
    remote.set_command(get_home_command)
    remote.button_was_pressed()

    print('Testing remote control with slots and undo')
    remote = RemoteControlWithUndo(3)

    garage_door_close_command = GarageDoorCloseCommand(GarageDoor(Light('Garage')))
    light_off_command = LightOffCommand(light)
    remote.set_command(0, garage_door_open_command, garage_door_close_command)
    remote.set_command(1, light_on_command, light_off_command)
    remote.on_button_was_pushed(0)
    remote.on_button_was_pushed(1)
    remote.undo_button_was_pushed()


if __name__ == '__main__':
    sys.exit(main())
