from Help_elements import create_button, create_label


class DishForm:
    def __init__(self, main, dish):
        self.dish = dish
        self.MainForm = main
        self.MainForm.window.title("Ресторан (Блюдо)")
        self.MainForm.create_console('Вы перешли на страницу блюда')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['dish_name_label'] = create_label(font_color = "#000000",
                                                                          text=f"Название блюда: {self.dish.name}",
                                                                          position=[500, 40], background = "#996600",
        font = "Sedan 14")
        self.MainForm.active_elements['type_of_dish_label'] = create_label(font_color = "#000000",
                                                                             text=f"Тип блюда: {self.dish.type_of_food}",
                                                                             position=[500, 80], background = "#996600",
        font = "Sedan 14")
        self.MainForm.active_elements['dish_quantity_label'] = create_label(font_color = "#000000",
                                                                                    text=f"Количество: {self.dish.quantity} шт.",
                                                                                    position=[850, 40], background = "#996600",
        font = "Sedan 14")
        self.MainForm.active_elements['dish_weight_label'] = create_label(font_color = "#000000",
                                                                          text=f"Вес порции: {self.dish.weight}г",
                                                                          position=[850, 80], background = "#996600",
        font = "Sedan 14")
        self.MainForm.active_elements['dish_cost_label'] = create_label(font_color = "#000000",
                                                                         text=f"Цена: {self.dish.cost}₽",
                                                                         position=[675, 120], background = "#996600",
        font = "Sedan 14")

        self.show_que_flag = False

        self.MainForm.active_elements['delete'] = create_button(font_color='#ffffff', text="Удалить",
                                                                 command=self.delete_dish,
                                                                 position=[470, 600], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")
        self.MainForm.active_elements['go_back'] = create_button(font_color = '#ffffff', text="Основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[730, 600], background = '#996633', width = '25', height = '3', font = "Sedan 12")

    def delete_dish(self):
        self.MainForm.dishes.remove(self.dish)
        self.MainForm.return_to_main_screen()

    def return_to_main_screen(self, text):
        self.MainForm.create_console(text)
        self.show_main_screen()
