class Food:
    def __init__(self, type_of_food, name, cost, quantity):
        self.type_of_food = type_of_food.lower().title()
        self.name = name.lower().title()
        self.cost = cost
        self.quantity = quantity

    def show_info(self):
        pass

    def get_full_name(self):
        return ''.join([self.name, ', Тип блюда: ', self.type_of_food, ', Цена блюда: ' , str(self.cost), '₽'])

    def get_name(self, number=None):
        if number is not None:
            return ''.join([self.name, ' (', str(number), ')'])
        return ''.join([self.name])

class OrderMain:
    def __init__ (self, table_number, sum_cost):
        self.table_number = table_number
        self.sum_cost = sum_cost
