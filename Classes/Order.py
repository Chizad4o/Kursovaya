from .Food import OrderMain

class Order(OrderMain):
    def __init__(self, table_number, dish1, dish2, dish3, dish4, dish5, sum_cost):
        super().__init__(table_number=table_number, sum_cost = sum_cost)
        self.dish1 = dish1
        self.dish2 = dish2
        self.dish3 = dish3
        self.dish4 = dish4
        self.dish5 = dish5

    def show_info(self):
        return ''.join(['Номер Столика: ', str(self.table_number), '; ', self.dish1, '  ', self.dish2, '  ', self.dish3, '  ', self.dish4, '  ', self.dish5, '\n Сумма Заказа: ', str(self.sum_cost), '₽'])
