"""CIS 189
Alex Rickels
Final Project - Tuscan Eatery"""

import datetime
from datetime import timedelta
import tkinter

# Unit tests 20
# Multiple Commits 10
# Class 10
# Input Validation 10
# Exception Handling 10
# Database 5
# GUI 5
# Code 20


class Order:

    def __init__(self, table, dishes_list=[]):
        '''
        :param table:  table # for the order, so other employee can bring food if ready
        :param dishes_list: dishes in the order
        '''

        if not 1 <= table <= 16:
            raise InvalidTableNumber
        self.__table = table
        menu_list = (
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
                raise InvalidDishError

        self.dishes_list = dishes_list

    def order_input(self):
        """
        :return: output of prep times for each dish in order
        """
        dish1 = dish1_entry.get()
        if dish1 == '':
            print("no order was submitted")
        else:
            self.dishes_list.append(dish1)

        dish2 = dish2_entry.get()
        if not dish2 == '':
            self.dishes_list.append(dish2)

        dish3 = dish3_entry.get()
        if not dish3 == '':
            self.dishes_list.append(dish3)

        dish4 = dish4_entry.get()
        if not dish4 == '':
            self.dishes_list.append(dish4)

        print(get_time(self.dishes_list))

    n = tkinter.Tk()
    n.title('Tuscan Eatery Order')

    table = tkinter.Label(n, text="Table: ", width=25)
    table.grid(row=6)
    table_entry = tkinter.Entry(n, width=25)
    table_entry.grid(row=6, column=2)

    dish1 = tkinter.Label(n, text="Dish 1: ", width=25)
    dish1.grid(row=2)
    dish1_entry = tkinter.Entry(n, width=25)
    dish1_entry.grid(row=2, column=2)

    dish2 = tkinter.Label(n, text="Dish 2: ", width=25)
    dish2.grid(row=3)
    dish2_entry = tkinter.Entry(n, width=25)
    dish2_entry.grid(row=3, column=2)

    dish3 = tkinter.Label(n, text="Dish 3: ", width=25)
    dish3.grid(row=4)
    dish3_entry = tkinter.Entry(n, width=25)
    dish3_entry.grid(row=4, column=2)

    dish4 = tkinter.Label(n, text="Dish 4: ", width=25)
    dish4.grid(row=5)
    dish4_entry = tkinter.Entry(n, width=25)
    dish4_entry.grid(row=5, column=2)

    n.mainloop()


class InvalidTableNumber(Exception):
    # This custom exception is raised if table # is not within specified range
    pass


class InvalidDishError(Exception):
    # This custom exception is dish is not on the menu
    pass


dish_dict = {
    'bruschetta': 5,
    'arugula salad': 3,
    'carbonara': 12,
    'spaghetti': 7,
    'risotto': 20,
    'focaccia': 3,
    'gelato': 2
}


def get_time(dish_list):
    """
    :param dish_list: list of dishes in order
    :return: time value of dish prep
    """
    for dish in dish_list:
        try:
            print('Begin ' + str(dish) + " at " + str(time(dish)))
        except KeyError:
            return KeyError


def time(dish):
    ready_time = (datetime.datetime.now() + timedelta(minutes=20))

    start_time = ready_time - timedelta(minutes=dish_dict[str(dish)])
    return start_time.strftime('%X')


# n = tkinter.Tk()
# n.title('Tuscan Eatery Order')
# button = tkinter.Button(n, text='Submit Order', width=25, command=Order().order_input())
# button.grid(row=7)
#
# table = tkinter.Label(n, text="Table: ", width=25)
# table.grid(row=6)
# table_entry = tkinter.Entry(n, width=25)
# table_entry.grid(row=6, column=2)
#
# dish1 = tkinter.Label(n, text="Dish 1: ", width=25)
# dish1.grid(row=2)
# dish1_entry = tkinter.Entry(n, width=25)
# dish1_entry.grid(row=2, column=2)
#
# dish2 = tkinter.Label(n, text="Dish 2: ", width=25)
# dish2.grid(row=3)
# dish2_entry = tkinter.Entry(n, width=25)
# dish2_entry.grid(row=3, column=2)
#
# dish3 = tkinter.Label(n, text="Dish 3: ", width=25)
# dish3.grid(row=4)
# dish3_entry = tkinter.Entry(n, width=25)
# dish3_entry.grid(row=4, column=2)
#
# dish4 = tkinter.Label(n, text="Dish 4: ", width=25)
# dish4.grid(row=5)
# dish4_entry = tkinter.Entry(n, width=25)
# dish4_entry.grid(row=5, column=2)
#
# n.mainloop()
