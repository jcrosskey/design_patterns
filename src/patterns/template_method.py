'''
Template Method Pattern

The Template Method Pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses.
Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

Its abstract class can define concrete methods, abstract methods, and hooks. Hooks do nothing or default behavior in the
abstract class, but may be overridden in the subclass. Some uses of hooks:
1. for a subclass to implement an optional part of an algorithm
1. give the subclass a chance to react to some step in teh template method that's about to happen (e.g. log messages,
   save checkpoint, etc. Think about git hooks.)
1. provide a subclass with the ability to make a decision for the abstract class.

Hollywood Principle guides us to put decision making in high-level modules that can decide how and when to call
low-level modules.

Related patterns: strategy (using composition while template method uses inheritance, both encapsulate algorithms);
factory method (a specialization of template method).
'''
from abc import ABC
from abc import abstractmethod
# A trivial example

class CacheError(Exception):
    """
    Exception raised for errors in loading/reading cache.
    """

class AbsClass(ABC):

    def template_method(self):
        self.operation1()
        self.operation2()
        self.__concrete_operation()
        self.hook()

    @abstractmethod
    def operation1(self):
        """
        Step 1 in the algorithm
        """

    @abstractmethod
    def operation2(self):
        """
        Step 2 in the algorithm
        """

    def __concrete_operation(self):
        print('I am a concrete operation shared by all subclasses, nobody should modify me')

    def hook(self):
        """
        Do pretty much nothing in the abstract class, but subclasses are welcome to use it
        for example, to do some clean up in the end.
        """
        return


# A more concrete example
class AbsCacheComputer(ABC):
    """
    Interface for algorithms using cache.
    """

    def run(self):
        """
        This is the skeleton of the algorithm.
        """
        result = None
        try:
            result = self.load_cache()
        except CacheError:
            result = self.compute()
            self.write_cache(result)
        finally:
            self.clean_up()
        return result

    @abstractmethod
    def load_cache(self):
        """
        Load from cache for the computation result, if load fails raise CacheError.
        """

    @abstractmethod
    def compute(self):
        """
        Perform computation, and return the result.
        """

    @abstractmethod
    def write_cache(self, result):
        """
        Save the result to cache.
        """

    def clean_up(self):
        """
        Default behavior is to do nothing.
        """
        pass
