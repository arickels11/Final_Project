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


class InvalidTableNumber(Exception):
    # This custom exception is raised if table # is not within specified range
    pass


class EnterTableNumber(Exception):
    # This custom exception if table # was left blank
    pass


class InvalidDishError(Exception):
    # This custom exception is dish is not on the menu
    pass

