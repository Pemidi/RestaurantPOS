from uuid import uuid4
from datetime import datetime


# DONE: Add Item class here
class Item:
    item_id = 1

    food_list = list()
    beverage_list = list()
    starter_list = list()

    def __init__(self, name, item_type, price):
        self.name = name
        self.item_type = item_type
        # self.count = count
        self.uuid = uuid4()
        self.check_item()
        self.datetime = datetime.now()
        self.price = price
        self.item_id = Item.item_id
        Item.item_id += 1


    def check_item(self):
        if self.item_type == 'f':
            Item.food_list.append(self)
        elif self.item_type == 'b':
            Item.beverage_list.append(self)
        elif self.item_type == 's':
            Item.starter_list.append(self)

# DONE: Add .sample() classmethod for Item which returns an instance:
#     def sample(self):
#         result = {
#             'name': 'item1'
    @classmethod
    def sample(cls):
        result = {
            'name': 'pizza',
            'item_type': 'f',
            'price': 1,
        }
        return cls(**result)
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

# DONE-2: Add item_id to the Item class, item_id should be auto incremental
# DONE-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# DONE-2: Change datetime attr to be assigned automatically in Item class
# DONE-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
