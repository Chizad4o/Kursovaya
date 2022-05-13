from .Food import Food      #импорт класса Food


class Dish(Food):           #класс, который заимствует данные из Food
    def __init__(self, type_of_food, name, cost, quantity, weight): #инизиализация экземпляров класса
        super().__init__(type_of_food=type_of_food, name=name,  cost = cost, quantity=quantity) #доступ к унаследованным методам и передача данных параметров
        self.weight = weight        #объявление собственной переменной

    def show_info(self):        #метод вывода информации о блюде, по названию, типу блюда, количеству, весу и цене
        return ''.join([self.name, ' Тип Блюда: ', self.type_of_food, ', Количество: ', str(self.quantity), 'шт. Вес блюда: ', str(self.weight), 'г, Цена: ', str(self.cost), ' ₽'])
