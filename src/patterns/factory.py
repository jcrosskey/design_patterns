"""
Factory Pattern (twofer!)

The Factory Method Pattern defines an interface for creating an object, but let subclasses "decide" which class to
instantiate. Factory Method lets a class defer instantiation to subclasses.

The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without
specifying their concrete classes.

Can we tell the differences between the 2 from the examples below?
"""

from abc import ABC
from abc import abstractmethod

#================================================================================
# Define pizzas
#================================================================================

class BasePizza(object):
    """
    Interface for all pizzas.
    """
    def __init__(self, name, dough, sauce, toppings=None):
        self.__name = name
        self.__dough = dough
        self.__sauce = sauce
        if toppings is None:
            toppings = list()
        self.__toppings = toppings.copy()

    def get_name(self):
        return self.__name

    def prepare(self):
        print(f'Preparing {self.__name}: tossing dough..., adding sauce..., adding toppings: {", ".join(self.__toppings)}')

    def bake(self):
        print(f'Baking {self.__name}')

    def cut(self):
        print(f'Cutting {self.__name}')

    def box(self):
        print(f'Boxing {self.__name}')

    def __str__(self):
        return (f'----{self.__name}----\n'
                f'{self.__dough}\n'
                f'{self.__sauce}\n'
                f'{", ".join(self.__toppings)}\n'
               )

# Some concrete pizzas!
class CheesePizza(BasePizza):
    def __init__(self):
        super().__init__(name='cheese pizza', dough='regular crust', sauce='marinara pizza sause',
                         toppings=['fresh mozzarella', 'parmesan'])

class ClamPizza(BasePizza):
    def __init__(self):
        super().__init__(name='clam pizza', dough='thin crust', sauce='white garlic sause',
                         toppings=['clams', 'grated parmesan cheese'])

class PepperoniPizza(BasePizza):
    def __init__(self):
        super().__init__(name='pepperoni pizza', dough='crust', sauce='marinara sause',
                         toppings=['sliced pepperoni', 'sliced onion', 'grated parmesan cheese'])

class VeggiePizza(BasePizza):
    def __init__(self):
        super().__init__(name='veggie pizza', dough='crust', sauce='marinara sause',
                         toppings=['shredded mozzarella', 'diced onion', 'grated parmesan cheese',
                                   'sliced mushrooms', 'sliced red pepper', 'sliced black olives'])

#================================================================================
# Very simple pizza factory and store, startup!
#================================================================================
class SimplePizzaFactory(object):
    """
    simple pizza factory, depending on concrete pizza classes (UGH!)
    """

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        else:
            raise RuntimeError(f'pizza type {pizza_type} cannot be made now')
        assert pizza is not None
        return pizza

class StartUpPizzaStore(object):
    """
    simple pizza store, depend on concrete factory, no polymorphism.
    """

    def __init__(self, factory):
        self.__factory = factory

    def order_pizza(self, pizza_type):
        pizza = self.__factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


#================================================================================
# Factory Method Stores!
# Time to franchise, we want stores at 2 locations with different styles: NY and Chicago
#================================================================================
class AbsPizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, pizza_type):
        """
        Returns BasePizza instance
        This is the "Factory Method".
        """

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

# It's kinda boring now, since NY and Chicago make exactly the same pizzas...
# In the real world where making money is more important than typing, we will type out
# more concrete pizza classes, such as NYStyleCheesePizza, ChicagoStyleCheesePizza, etc...

# For now, let's settle with toy pizza stores.
class NYFmPizzaStore(AbsPizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        else:
            raise RuntimeError(f'pizza type {pizza_type} cannot be made now')
        assert pizza is not None
        return pizza


class ChicagoFmPizzaStore(AbsPizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        else:
            raise RuntimeError(f'pizza type {pizza_type} cannot be made now')
        assert pizza is not None
        return pizza

#================================================================================
# Abstract Factory Stores!
# Now we want the pizzas to have exactly the ingredients specified by corporation,
# stores cannot just change them on a whim! But fresh clams are not as easy to get 
# in Chicago as in NY..
#================================================================================

# The magic here is to "abstract" the factory that creates the ingredients for pizzas.

# Ah we also need to define classes for these ingredients.Ingredients
# have different qualities at different locations.
# Again, to save typing time, our pizza only has 2 ingredients: dough and clams..

class AbsDough(ABC):

    @abstractmethod
    def to_string(self):
        """
        """

class ThinCrustDough(AbsDough):

    def to_string(self):
        return "Thin Crust Dough"

class ThickCrustDough(AbsDough):

    def to_string(self):
        return "ThickCrust style extra thick crust dough"

class AbsClams(ABC):

    @abstractmethod
    def to_string(self):
        """
        """

class FreshClams(AbsClams):

    def to_string(self):
        return "Fresh Clams from Long Island Sound"

class FrozenClams(AbsClams):

    def to_string(self):
        return "Frozen Clams from Chesapeake Bay"
## Buy more ingredients...


class AbsIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self):
        """
        """

    @abstractmethod
    def create_clam(self):
        """
        """

## Buy more ingredients...

class NYIngredientFactory(AbsIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_clam(self):
        return FreshClams()

class ChicagoIngredientFactory(AbsIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_clam(self):
        return FrozenClams()

## Open more ingredient factories... California?


class AfClamPizza(BasePizza):
    def __init__(self, ingredient_factory):
        self.__ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.get_name()}')
        dough = self.__ingredient_factory.create_dough()
        clam = self.__ingredient_factory.create_clam()

## Put more pizza types on the menu...

class NYAfPizzaStore(AbsPizzaStore):

    def create_pizza(self, pizza_type):
        ingredient_factory = NYIngredientFactory()
        pizza = None
        if pizza_type == 'clam':
            pizza = AfClamPizza(ingredient_factory)
        else:
            raise RuntimeError(f'unfortunately only clam pizza is available')
        return pizza

## More concrete pizza stores...

class Main(object):
    """
    $ python src/patterns/factory.py
    """

    def main(self):
        print('Test drive start up pizza store')
        simple_factory = SimplePizzaFactory()
        store = StartUpPizzaStore(simple_factory)

        pizza = store.order_pizza('clam')
        print(f'We ordered a {pizza.get_name()} pizza.\n')

        pizza = store.order_pizza('veggie')
        print(f'We ordered a {pizza.get_name()} pizza.\n')

if __name__ == '__main__':
    Main().main()
