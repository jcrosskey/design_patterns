'''
Composite Pattern

The composite pattern allows you to compose objects into tree structures to represent
part-whole hierarchies. Composite lets clients treat individual objects and compositions of
object uniformly.

The composite pattern does not have a "single responsibility"! It manages a hierarchy AND
it performs operations related to its components. In this case, Composite Pattern trades the Single
Responsibility design principle for _transparency_.

In most cases, we can ignore the differences between compositions of objects and individual objects.
'''


class MenuComponent(object):
    '''
    Interface for the menu component, provides default implementation for all the methods.
    '''

    def add(self, menu_component):
        """
        Add `menu_component` as part of the MenuComponent composite

        Parameters
        ----------
        menu_component : MenuComponent
            A component to add to the MenuComponent instance

        """
        assert isinstance(menu_component, MenuComponent)
        raise NotImplementedError()

    def remove(self, menu_component):
        assert isinstance(menu_component, MenuComponent)
        raise NotImplementedError()

    def get_child(self, idx):
        assert isinstance(idx, int) and idx >= 0
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()

    def get_description(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def is_vegetarian(self):
        raise NotImplementedError()

    def print_menu(self):
        raise NotImplementedError()
