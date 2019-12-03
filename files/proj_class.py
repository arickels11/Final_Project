"""CIS 189
Alex Rickels
Final Project - Tuscan Eatery"""

import datetime
from datetime import timedelta


class Order:

    def __init__(self, table, dishes_list=[]):
        '''
        :param table:  table # for the order, so other employee can bring food if ready
        :param dishes_list: dishes in the order
        '''
        if table == '':  # input validation
            raise EnterTableNumber  # exception handling
        nums = set("1234567890")  # input validation
        if not nums.issuperset(table):
            raise InvalidTableNumber  # exception handling
        if not 1 <= int(table) <= 16:  # input validation
            raise InvalidTableNumber   # exception handling
        self.table = table
        if len(dishes_list) == 0:  # input validation
            raise MissingOrderError  # exception handling
        menu_list = (  # list, input validation
            'bruschetta',
            'arugula salad',
            'carbonara',
            'spaghetti',
            'risotto',
            'focaccia',
            'gelato'
        )

        for item in dishes_list:
            if item not in menu_list:
                raise InvalidDishError  # exception handling

        self.dishes_list = dishes_list

    def change_table(self, table):
        self.table = table

    def update_dishes_list(self, dishes_list):
        self.dishes_list = dishes_list

    def order_input(self):
        return str(self.print_table()) + str(self.get_time())  # prints table # and order with prep time for each dish

    def print_table(self):
        print('Table:', self.table)

    def get_time(self):
        """
        :return: time value of dish prep
        """

        def time(dish):
            dish_dict = {  # dictionary for all menu items and corresponding preparation time of each
                'bruschetta': 5,
                'arugula salad': 3,
                'carbonara': 12,
                'spaghetti': 7,
                'risotto': 20,
                'focaccia': 3,
                'gelato': 2
            }
            ready_time = datetime.datetime.now() + timedelta(minutes=20)  # ready time is now + 20 minutes
            dish_time = dish_dict[str(dish)]
            start_time = ready_time - timedelta(minutes=dish_time)  # start time= order time - prep time(from dish dict)
            return start_time.strftime('%X')  # formatting for only time, no date

        for dish in self.dishes_list:
                prep_time = str(time(dish))
                print('Begin ' + str(dish) + " at " + prep_time)  # prints prep time for each dish in order


class InvalidTableNumber(Exception):
    # This custom exception is raised if table # is not within specified range
    pass


class EnterTableNumber(Exception):
    # This custom exception if table # was left blank
    pass


class InvalidDishError(Exception):
    # This custom exception is dish is not on the menu
    pass


class MissingOrderError(Exception):
    # This custom exception is if no dishes are entered in order
    pass

