from .Food import OrderMain

class Order(OrderMain):
    def __init__(self, table_number, dish1, dish2, dish3, dish4, dish5, sum_cost, quantity1, quantity2, quantity3, quantity4, quantity5):   #инизиализация экземпляров класса
        super().__init__(table_number=table_number, sum_cost = sum_cost)
        self.dish1 = dish1  #объявление собстевнной перемнной, которая является копией dish1
        self.dish2 = dish2  #объявление собстевнной перемнной, которая является копией dish2
        self.dish3 = dish3  #объявление собстевнной перемнной, которая является копией dish3
        self.dish4 = dish4  #объявление собстевнной перемнной, которая является копией dish4
        self.dish5 = dish5  #объявление собстевнной перемнной, которая является копией dish5
        self.quantity1 = quantity1  #объявление собстевнной перемнной, которая является копией quantity1
        self.quantity2 = quantity2  #объявление собстевнной перемнной, которая является копией quantity2
        self.quantity3 = quantity3  #объявление собстевнной перемнной, которая является копией quantity3
        self.quantity4 = quantity4  #объявление собстевнной перемнной, которая является копией quantity4
        self.quantity5 = quantity5  #объявление собстевнной перемнной, которая является копией quantity5


    def show_info(self):        #метод для вывода информации о заказе
        return ''.join(['Номер Столика: ', str(self.table_number), '; ', self.dish1, ' ', str(self.quantity1), '  ', self.dish2, ' ', str(self.quantity2), '  ',
                        self.dish3, ' ', str(self.quantity3), '  ', self.dish4, ' ', str(self.quantity4), '  ',  self.dish5, ' ', str(self.quantity5), '\n Сумма Заказа: ', str(self.sum_cost), '₽'])
