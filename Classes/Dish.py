from .Food import Food


class Dish(Food):
    def __init__(self, type_of_food, name, cost, quantity, weight):
        super().__init__(type_of_food=type_of_food, name=name,  cost = cost, quantity=quantity)
        self.weight = weight

    def show_info(self):
        return ''.join([self.name, ' Тип Блюда: ', self.type_of_food, ', Количество: ', str(self.quantity), 'шт. Вес блюда: ', str(self.weight), 'г, Цена: ', str(self.cost), ' ₽'])