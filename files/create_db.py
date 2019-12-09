"""CIS 189
Alex Rickels
Final Project - Tuscan Eatery"""
from files.db_class import *

if __name__ == '__main__':

    order_db = OrderDatabase()
    # order_db.create_tables()
    print(order_db.select_all_orders())
