from dataclasses import dataclass, field
from Task3 import Food, Drink, Item


@dataclass
class Customer:
	# all the variables with the class are private
	__name: str = field(default=0)
	__numberOfCustomers: int = field(default=0)
	__id: int = field(default=0)
	__dateOfBirth: str = field(default="Not assigned")
	__nationality: str = field(default="Not assigned")
	__shopping_list: list = field(default="Shopping list is empty")

	def __init__(self, name, shopping_list=None):     # constructor accepts customer name and shopping cart
		if shopping_list is None:
			shopping_list = []
		self.__name = name
		self.__shopping_list = shopping_list
		Customer.__numberOfCustomers += 1             # number of customers is tracked here
		self.__id = (Customer.__numberOfCustomers - 1) + 1    # id of customers is tracked here

	# method returning id of an instance
	def get_identifier(self):
		return "Id of " + self.__name + " is " + str(self.__id)

	# method returning name and id of an instance
	def get_full_info(self):
		full_info = self.__name + " with id=" + str(self.__id)
		return full_info

	# method assigning the date of birth to the customer instance (returns log of an action)
	def assign_dob(self, new_dob):
		self.__dateOfBirth = new_dob
		print("*Date of birth was set to " + new_dob + "*")

	# method returning the date of birth of the customer instance
	def retrieve_dob(self):
		return "Date of birth of " + self.__name + " is " + self.__dateOfBirth

	# method assigning the nationality to the customer instance (returns log of an action)
	def assign_nationality(self, new_nationality):
		self.__nationality = new_nationality
		print("*Nationality was set to " + new_nationality + "*")

	# method returning the nationality of the customer instance
	def retrieve_nationality(self):
		return "Nationality of " + self.__name + " is " + self.__nationality

	# method returning number of customers
	@staticmethod
	def get_number_of_customers():
		return "Number of customers is " + str(Customer.__numberOfCustomers)

	# method for adding an item to the customer shopping list
	def add_item(self, item):
		self.__shopping_list.append(item)

	# method for removing an item from the customer shopping list
	def remove_item(self, index):
		if index <= len(self.__shopping_list):
			del self.__shopping_list[index]
		else:
			print('Error deleting an item from the list. There is no item in the list with such index. The maximum index is '
			  + str(len(self.__shopping_list)) + "\n")

	# method returning the items in customer shopping list
	def get_items(self):
		print("Items in the shopping list: \n")
		items_list = '\n'.join(map(str, self.__shopping_list))
		return items_list


# --------DEMO--------
# CREATING AN INSTANCE OF A CLASS CUSTOMER PASSING NAME AND ITEM
c1 = Customer("Jonas Jonaitis", [Food("Pizza", 12, 1.5)])

# ADDING TWO DIFFERENT ITEMS TO THE SHOPPING CART
c1.add_item(Food("Kebab", 10, 4.5))
c1.add_item(Drink("Cola", 2, 1))

# REMOVING THE ITEM WITH INDEX 1 FROM THE SHOPPING CART
c1.remove_item(1)

# PRINTING ALL ITEMS FROM THE CUSTOMER SHOPPING LIST
print(c1.get_items())
