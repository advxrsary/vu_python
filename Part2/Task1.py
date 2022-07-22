from dataclasses import dataclass, field


@dataclass
class Customer:
	__name: str = field(default=0, repr=False)
	__numberOfCustomers: int = field(default=0, repr=False)
	__id: int = field(default=0, repr=False)
	__dateOfBirth: str = field(default="Not assigned", repr=False)
	__nationality: str = field(default="Not assigned", repr=False)
	
	def __init__(self, name):
		self.__name = name
		Customer.__numberOfCustomers += 1
		self.__id = (Customer.__numberOfCustomers -1) + 1

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


# --------DEMO--------

# creating 3 instances of a class Customer passing different names

# c1 = Customer("Pavel Yushkevich")
# c2 = Customer("Sevastian Zare")
# c3 = Customer("Kiryl Andreyeu")

# PRINTING ID's of the customers
# print(c1.get_identifier())
# print(c2.get_identifier())
# print(c3.get_identifier())

# PRINTING NAME AND IDs OF THE CUSTOMERS
# print(c1.get_full_info())
# print(c2.get_full_info())
# print(c3.get_full_info())

# RETRIEVING THE DATE OF BIRTH OF THE CUSTOMER
# print(c1.retrieve_dob())

# ASSIGNING THE DATE OF BIRTH AND RETRIEVING IT AGAIN
# c1.assign_dob("2002.06.17")
# print(c1.retrieve_dob())

# retrieving the nationality of customer
# print(c1.retrieve_nationality())

# ASSIGNING THE NATIONALITY AND RETRIEVING IT AGAIN
# c1.assign_nationality("Belarus")
# print(c1.retrieve_nationality())

# GETTING THE NUMBER OF CUSTOMERS
# print(Customer.get_number_of_customers())
