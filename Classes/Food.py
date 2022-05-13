class Food:
    def __init__(self, type_of_food, name, cost, quantity): #инизиализация экземпляров класса
        self.type_of_food = type_of_food.lower().title()    #объявление собстевнной перемнной, которая является копией type_of_food
        self.name = name.lower().title()    #объявление собстевнной перемнной, которая является копией name
        self.cost = cost    #объявление собстевнной перемнной, которая является копией cost
        self.quantity = quantity    #объявление собстевнной перемнной, которая является копией quantity

    def show_info(self):    #метод для показывания информации
        pass

    def get_full_name(self):    #метод для вывода информации о блюде
        return ''.join([self.name, ', Тип блюда: ', self.type_of_food, ', Цена блюда: ' , str(self.cost), '₽'])

    def get_name(self, number=None):    #метода для вывода названия блюд с цифрами, для метода поиска по названию(формирование перечная названий блюд
        if number is not None:
            return ''.join([self.name, ' (', str(number), ')'])
        return ''.join([self.name])

class OrderMain:        #класc OrderMain
    def __init__ (self, table_number, sum_cost):
        self.table_number = table_number    #объявление собстевнной перемнной, которая является копией table_number
        self.sum_cost = sum_cost    #объявление собстевнной перемнной, которая является копией sum_cost
