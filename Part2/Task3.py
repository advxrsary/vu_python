from dataclasses import dataclass, field                        # import of additional modules dataclass and field, from library dataclasses.


@dataclass                                                      # declaring that this class is going to be dataclass
class Item:                                                     # class Item describes three item characteristics – name, count and price.
    dict = {}                                                   # declaration of the dictionary.
    name: str                                                   # declaration of the name variable.
    count: int = field(default=1)                               # declaration of the count variable.
    price: float = field(default=10.0)                          # declaration of the price variable.

    def get_total_price(self):                                  # method for calculating total price of the item (multiplies count on price).
        return self.count * self.price                          # returns value of the calculation.

    def full_info(self):                                        # method for printing all information about the item (name, count, price, total price).
        return self.name, self.count, self.price, self.get_total_price()      # returns full information of the item.

    def to_dict(self):                                          # method for insertion of the values into the dictionary
        self.dict['name'] = self.name                           # key 'name' equals name of the item
        self.dict['count'] = self.count                         # key 'name' count name of the count
        self.dict['price'] = self.price                         # key 'name' price name of the price
        return self.dict                                        # returns keys and its values


@dataclass
class Food(Item):
    def full_info(self):                                                        # method for printing all information about the item (name, count, price, total price).
        return self.name, self.count, self.price, self.get_total_price()        # returns a string with full information of the item.


class Drink(Item):
    def full_info(self):                                                        # method for printing all information about the item (name, count, price, total price).
        return self.name, self.count, self.price, self.get_total_price()        # returns a string with full information of the item.


f1 = Food("Bread", 2, price=0.5)    # creating a variable and assigning values for the first item of class Food()
f2 = Food("Butter", 1, 1.3)         # creating a variable and assigning values for the second item of class Food()

d1 = Drink("Bread", 2, price=0.5)   # creating a variable and assigning values for the first item of class Drinks()
d2 = Drink("Sprite", 2, 1.7)        # creating a variable and assigning values for the second item of class Drinks()
