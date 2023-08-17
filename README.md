# design_patterns

This is a repository with python implementation of design patterns from [Head First Design Patterns](http://shop.oreilly.com/product/9780596007126.do), which uses java mainly.

There are also some sample implementations of patterns from [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612/ref=pd_lpo_sbs_14_t_0?_encoding=UTF8&psc=1&refRID=T5MT0MSKYV58JHR0R6P8). This is the classic book on design patterns and includes more patterns than the first book.

Some excerpt from these books is cited in the docstring.

# Patterns Summary

## Strategy Pattern
* Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
* Different algorithms can be swapped at run time (dynamically) as well.
* Questions
  - Why is called "strategy pattern"?
  - Examples where this pattern can/should be used?

## Factory Pattern

### factory method pattern

The Factory Method Pattern defines an interface for creating an object, but let subclasses "decide" which class to
instantiate. Factory Method lets a class defer instantiation to subclasses.

* It's an abstract method so subclasses must implement it.
  - One can also define a default factory method to produce a concrete object.
* It returns a Product that's typically used within methods defined in the superclass.
* It isolates the client from knowing what kind of concrete Product is actually created, instead the client only knows
  the Product is of a super type.
  - Python does not declare the type of returned object, so the client has to ensure a Product of the correct type is returned.
  - `abstract Pizza createPizza(String pizzaType)` in Java, or

    ```python
    @abstractmethod 
    def create_pizza(self, pizza_type):
        """
        Returns
        -------
        pizza: Pizza
        """

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        assert isinstance(pizza, Pizza)
        ...
    ```
* It decouples the creation (implementation) of a Product from its use.

### abstract factory pattern

The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without
specifying their concrete classes.

Factory methods are a natural way to implement your product methods in your abstract factories.

### Compared
1. Factory Method is used to decouple client code from concrete classes you need to instantiate, it's also helpful if
   you don't know ahead of time all the concrete classes needed.
1. Abstract Factory should be used whenever you have families of products you need to create and you want to make sure
   your clients create products that belong together.
