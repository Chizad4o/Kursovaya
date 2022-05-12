from Help_elements import create_button, create_entry, create_label, create_combo_box
from constants import MAXCOST, MAXLENNAME, VALUE, TYPE_OF_FOOD, MAXWEIGHT, MAXQUANTITY
from checker import name_checker, cost_checker, quantity_checker, weight_checker
from .Dish import Dish


class AdminForm:
    def __init__(self, main):
        self.MainForm = main
        self.MainForm.window.title("Ресторан (администратор)")
        self.MainForm.create_console('Переход на панель администратора')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.active_elements['admin_label'] = create_label(font_color="#000000",
                                                                    text="Вы находитесь в панели администратора, что "
                                                                         "делать с рестораном?",
                                                                    position=[400, 40], background="#996600",
                                                                    font="Sedan 14")
        self.MainForm.active_elements['dish_help_label'] = create_label(font_color="#000000",
                                                                          text=f"Количество блюд в ресторане сейчас: {str(len(self.MainForm.dishes))}",
                                                                          position=[400, 80], background="#996600",
                                                                          font="Sedan 14")
        self.MainForm.active_elements['chose_what_do'] = create_label(font_color="#000000",
                                                                      text=f"Выберите действие:",
                                                                      position=[250, 600], background="#996600",
                                                                      font="Sedan 14")
        self.MainForm.active_elements['add_dish'] = create_button(font_color='#ffffff',
                                                                    text="Добавить Блюдо",
                                                                    command=self.add_dish,
                                                                    position=[480, 600], background='#996633',
                                                                    width='25', height='3', font="Sedan 12")
        self.MainForm.active_elements['find_cost'] = create_label(font_color="#000000",
                                                                           text=f"Поиск по цене",
                                                                           position=[1000, 400], background="#996600",
                                                                           font="Sedan 14")
        self.MainForm.active_elements['find_cost_combo'] = create_combo_box(width=12, font_color="#000000",
                                                                               position=[1000, 450],
                                                                               values=VALUE, default=None,
                                                                               callback=self.show_find_cost, font="Sedan 14")
        self.MainForm.active_elements['show_dishes'] = create_button(font_color='#ffffff',
                                                                      text="Показать блюда",
                                                                      command=self.show_all_dishes,
                                                                      position=[740, 600], background='#996633',
                                                                      width='25', height='3', font="Sedan 12")
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff',
                                                                 text="Вернуться на основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1150, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")
    def show_find_cost(self, event):
        exp_radius = self.MainForm.active_elements.get('find_cost_combo').get()
        text = f"Блюд с ценой {exp_radius}:"
        count = 1
        if exp_radius[0] == "0":
            start_exp = 0
        else:
            start_exp = int(exp_radius[:3])
        stop_exp = int(exp_radius[-3] + exp_radius[-2] + exp_radius[-1])
        for dish in self.MainForm.dishes:
            if dish.cost in [i for i in range(start_exp, stop_exp+1)]:
                text += f'\n{count}) {dish.get_full_name()}'
                count += 1
        if text == f"Блюд с ценой {exp_radius}:":
            text += "\nПо вашему запросу ничего не найдено"
        self.MainForm.create_console(text)

    def return_to_admin_screen(self):
        self.MainForm.create_console('Возврат в панель администратора')
        self.MainForm.destroy_all()
        self.show_main_screen()

    def add_dish(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console('Переход на страницу добавления доктора')
        self.MainForm.active_elements['dish_label'] = create_label(font_color="#000000",
                                                                     text="Страница добавления блюда",
                                                                     position=[400, 40], background="#996600",
                                                                     font="Sedan 14")
        self.MainForm.active_elements['dish_name'] = create_label(font_color="#000000",
                                                                       text="Название блюда", position=[140, 150],
                                                                       background="#996600",
                                                                       font="Sedan 14")
        self.MainForm.active_elements['dish_name_entry'] = create_entry(width=25, font="Sedan 14",
                                                                             position=[140, 200], font_color="#000000")
        self.MainForm.active_elements['dish_type_of_food'] = create_label(font_color="#000000",
                                                                    text="Тип блюда", position=[140, 250],
                                                                    background="#996600",
                                                                    font="Sedan 14")
        self.MainForm.active_elements['dish_type_of_food_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 300],
                                                                              values=TYPE_OF_FOOD,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['dish_quantity'] = create_label(font_color="#000000",
                                                                              text="Количество блюд",
                                                                              position=[140, 350], background="#996600",
                                                                              font="Sedan 14")
        self.MainForm.active_elements['dish_quantity_entry'] = create_entry(width=25, font="Sedan 14",
                                                                                    position=[140, 400],
                                                                                    font_color="#000000")
        self.MainForm.active_elements['dish_weight'] = create_label(font_color="#000000",
                                                                    text="Вес блюда", position=[140, 450],
                                                                    background="#996600",
                                                                    font="Sedan 14")

        self.MainForm.active_elements['dish_weight_entry'] = create_entry(width=25, font="Sedan 14",
                                                                          position=[140, 500],
                                                                          font_color="#000000")
        self.MainForm.active_elements['dish_cost'] = create_label(font_color="#000000",
                                                                          text="Цена Блюда", position=[140, 550],
                                                                          background="#996600",
                                                                          font="Sedan 14")
        self.MainForm.active_elements['dish_cost_entry'] = create_entry(width=25, font="Sedan 14",
                                                                                position=[140, 600],
                                                                                font_color="#000000")
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")
        self.MainForm.active_elements['complete'] = create_button(font_color='#ffffff', text="Выполнить",
                                                                  command=self.add_new_dish, position=[190, 650],
                                                                  background='#996633', width=20, height='3',
                                                                  font="Sedan 12")

    def add_new_dish(self):
        type_of_food = self.MainForm.active_elements['dish_type_of_food_entry'].get()
        name, name_flag = name_checker(self.MainForm.active_elements['dish_name_entry'].get())
        cost, cost_flag = cost_checker(self.MainForm.active_elements['dish_cost_entry'].get())
        quantity, quantity_flag = quantity_checker(self.MainForm.active_elements['dish_quantity_entry'].get())
        weight, weight_flag = weight_checker(self.MainForm.active_elements['dish_weight_entry'].get())
        if not name_flag:
            self.MainForm.create_console(
                f"Название блюда введено неверно\n Учтите что длина названия не может превышать {MAXLENNAME} символов\nи не должна содержать цифры")
        if not cost_flag:
            self.MainForm.create_console(
                f"Цена введена неверно\n Учтите что цена не может превышать {MAXCOST} ₽ \nили быть меньше 0 ₽")
        if not quantity_flag:
            self.MainForm.create_console(
                f"Количество введено неверно\n Учтите что количество не может превышать {MAXQUANTITY} \nили быть меньше 0")
        if not weight_flag:
            self.MainForm.create_console(
                f"Вес введен неверно\n Учтите что вес не может превышать {MAXWEIGHT} \nили быть меньше 0")
        exsist_flag = True
        if name_flag and quantity_flag and cost_flag and weight_flag:
            for dish in self.MainForm.dishes:
                print(dish.type_of_food, type_of_food)
                if dish.type_of_food == type_of_food.lower().title() and dish.name == name.lower().title() and dish.quantity == quantity and dish.cost == cost and dish.weight == weight:
                    exsist_flag = False
                    break
        if not exsist_flag:
            self.MainForm.create_console(
                f"Такое блюдо уже существует")
        if name_flag and quantity_flag and cost_flag and exsist_flag:
            self.MainForm.dishes.append(
                Dish(type_of_food=type_of_food, name=name, cost=cost, quantity=quantity, weight = weight))
            self.return_to_admin_screen()

    def show_all_dishes(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")

        text = ""
        count = 1
        for dish in self.MainForm.dishes:
            text = ''.join([text, f'\n{count}) ', dish.show_info()])
            count += 1
        if text == "":
            text += "Блюд пока нет"
        self.MainForm.create_big_console(text)
