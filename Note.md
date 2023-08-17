## OO Basics

* Abstraction
* Encapsulation
* Polymorphism
* Inheritance

## OO principles
* Encapsulate what varies
* Favor composition over inheritance
* Program to interfaces, not implementations
* Strive for loosely coupled designs between objects that interact
* Classes should be open for extension, but closed for modification.
    - Applying the open-closed principle EVERYWHERE is wasteful and unnecessary, and can lead to complex, hard-to-understand code.
    - When the code uses a lot of concrete classes, it has to be changed as new concrete classes are added. In other
      words, the code will not be "closed for modification". To extend it with new concrete types, you'll have to reopen
      it.
* Dependency Inversion Principle: Depend upon abstractions. Do not depend on concrete classes.
    - High level components should not depend on low-level components; rather, they should both depend on abstractions.
    - Reduce dependency on concrete classes.
    - Some guidelines:
        1. No variable should hold a reference to a concrete class
        1. No class should derive from a concrete class
        1. No method should override an implemented method of any of its base classes
