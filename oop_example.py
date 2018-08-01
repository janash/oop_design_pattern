"""
    Example of using OOP in Python 3
"""
# library to import to make classes abstract
import abc

class AbstractOrder(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def order_details(self):
        pass

    def hello_from_parent(self):
        print("Hello from Parent class, Abstract")


class Order(AbstractOrder):

    # class attribute
    _in_stock = 10

    def __init__(self, num_items=0, name=None):

        # num public
        # _num protected/private
        # __num private

        # Call init __init__ for Parent - Python 3 ONLY
        super().__init__(name)

       #  super(Order, self).__init__(name) # python 2, 3

        self.num_items = num_items
        self._in_stock -= self.num_items

    def order_details(self):
        return "{} ordered {} items".format(self.name, self.num_items)

    # class method
    @classmethod
    def class_method(cls):
        print("In stock: {}".format(cls._in_stock))

    # static method - 'doesn't have access to class'. 'it's useless' says Doaa (just her opinion)
    @staticmethod
    def static_method():
        print("I don't know my class.")


class StoreOrder(Order):
    
    # method override
    def order_details(self):
        return "In store ordered {} items.".format(self.num_items)



try:
    order = AbstractOrder()
except Exception as err:
    print(err)
