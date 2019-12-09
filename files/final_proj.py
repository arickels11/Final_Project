"""CIS 189
Alex Rickels
Final Project - Tuscan Eatery"""

import datetime
from datetime import timedelta
import tkinter
from files.ord_class import Order
from files.db_class import *


class InvalidTableNumber(Exception):
    # This custom exception is raised if table # is not within specified range
    pass


class EnterTableNumber(Exception):
    # This custom exception is raised if table # is not within specified range
    pass


class InvalidDishError(Exception):
    # This custom exception is dish is not on the menu
    pass


class MissingOrderError(Exception):
    # This custom exception is if no dishes are entered in order
    pass


dish_dict = {  # dictionary for all menu items and corresponding preparation time
    'bruschetta': 5,
    'arugula salad': 3,
    'carbonara': 12,
    'spaghetti': 7,
    'risotto': 20,
    'focaccia': 3,
    'gelato': 2
}


def order_input():
    """
    :return: output of prep times for each dish in order
    """

    order_list = []

    order_db = OrderDatabase()
    if table_entry.get() == '':  # input validation - table field not left blank
        raise EnterTableNumber  # exception handling
    else:
        try:
            table_num = int(table_entry.get())  # input validation - only tables 1 - 16
            if not 1 <= table_num <= 16:
                raise InvalidTableNumber
            else:
                pass
        except ValueError:
            raise InvalidTableNumber  # exception handling

    dish1 = dish1_entry.get()
    if dish1 == '':
        raise MissingOrderError
    else:
        order_list.append(dish1)

    dish2 = dish2_entry.get()
    if not dish2 == '':
        order_list.append(dish2)

    dish3 = dish3_entry.get()
    if not dish3 == '':
        order_list.append(dish3)

    dish4 = dish4_entry.get()
    if not dish4 == '':
        order_list.append(dish4)

    order = Order(table_num, order_list)
    order_db.insert_order(order)
    text_output.insert(tkinter.END, str(print_table(order.table)) + str(get_time(order.dishes_list)))


def print_table(table_number):
    return 'Table:' + str(table_number) + '\n'


def get_time(dish_list):
    """
    :param dish_list: list of dishes in order
    :return: time value of dish prep
    """

    menu_list = (  # list of menu items for input validation
        'bruschetta',
        'arugula salad',
        'carbonara',
        'spaghetti',
        'risotto',
        'focaccia',
        'gelato'
    )

    dish_output = ""

    for dish in dish_list:
        if dish not in menu_list:  # input validation - only dishes in menu can be ordered
            raise InvalidDishError  # exception handling
        else:
            prep_time = str(time(dish))
            dish_output = dish_output + 'Begin ' + str(dish) + " at " + prep_time + "\n"
    return dish_output


def time(dish):
    ready_time = (datetime.datetime.now() + timedelta(minutes=20))
    try:
        dish_time = dish_dict[str(dish)]
        start_time = ready_time - timedelta(minutes=dish_time)
        return start_time.strftime('%X')
    except KeyError:
        return KeyError


n = tkinter.Tk()
n.title('Tuscan Eatery Order')


table = tkinter.Label(n, text="TABLE (1-16): ", width=25, font='bold')
table.grid(row=1)
table_entry = tkinter.Entry(n, width=25)
table_entry.grid(row=1, column=2)

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

button = tkinter.Button(n, text='Submit Order', width=25, command=order_input)
button.grid(row=7)

button = tkinter.Button(n, text='Cancel Screen', width=25, command=n.destroy)
button.grid(row=8)

text_output = tkinter.Text(n, height=6, width=35)
text_output.grid(row=9)

n.mainloop()
