import tkinter as tk
from Help_elements import create_button, create_entry, create_label, create_combo_box
from checker import check_correct_admin_password, name_checker, cost_checker, quantity_checker, weight_checker
from .AdminForm import AdminForm
from .DishForm import DishForm
from .OrderForm import OrderForm
from constants import CONSOLETEXT, TYPE_OF_FOOD, VALUE
import os
import pandas as pd
from .Dish import Dish


class MainForm:
    def __init__(self):
        self.dish_auth_active = None
        self.dishes, self.order, self.patients = [], [], []
        self.dish_ques = {}
        for name_type_of_food in TYPE_OF_FOOD:
            self.dish_ques[name_type_of_food] = []
        self.active_elements = {}
        self.window = tk.Tk()
        self.window.geometry('1400x875')

        background = tk.PhotoImage(file=os.path.abspath(os.path.join('background.png')))
        self.__background_label = tk.Label(self.window, image=background)
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label_name = tk.PhotoImage(file=os.path.abspath(os.path.join('label.png')))
        self.__secret_label = tk.Label(self.window, image=label_name, background='#996633')
        self.__secret_label.place(x=1, y=1)

        self.show_main_screen()
        self.create_console()
        self.window.mainloop()

    def create_console(self, text=""):
        create_label(font_color='#000000',
                     text=CONSOLETEXT, position=[430, 175], font="Sedan 14", background="#996600")

        label = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=50,
            height=16,
        )
        label.place(x=440, y=225)

    def create_big_console(self, text=""):
        self.active_elements['big_console'] = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=100,
            height=22,
        )
        self.active_elements['big_console'].place(x=150, y=200)

    def show_main_screen(self):
        self.destroy_all()
        self.window.title("Ресторан")
        self.active_elements['chose_what_do'] = create_label(font_color='#000000', text="Выберите действие:",
                                                             position=[250, 700], background="#996600", font="Sedan 14")
        self.active_elements['admin_button'] = create_button(font_color='#ffffff', text="Войти как админ",
                                                             command=self.show_admin_auth, position=[240, 600],
                                                             background='#996633', width='25',
                                                             height='3', font="Sedan 12")
        self.dish_auth_active = False
        self.now_dishes = []
        self.now_orders = []
        self.active_elements['dish_button'] = create_button(font_color='#ffffff', text="Поиск/Удаление блюда",
                                                            command=self.show_dishes, position=[500, 600],
                                                            background='#996633', width='25',
                                                            height='3', font="Sedan 12")
        self.patient_auth_active = False
        self.active_elements['new_order_button'] = create_button(font_color='#ffffff', text="Добавить заказ",
                                                                 command=self.add_order, position=[760, 600],
                                                                 background='#996633', width='25',
                                                                 height='3', font="Sedan 12")
        self.active_elements['order_show_button'] = create_button(font_color='#ffffff', text="Заказы",
                                                                  command=self.show_all_orders, position=[760, 700],
                                                                  background='#996633', width='25',
                                                                  height='3', font="Sedan 12")
        self.active_elements['show_menu'] = create_button(font_color='#ffffff', text="Меню",
                                                                 command=self.show_menu, position=[500, 700],
                                                                 background='#996633', width='25', height='3',
                                                                 font="Sedan 12")
        self.file_flag = False
        self.active_elements['copy_file_btn'] = create_button(font_color='#ffffff', text="Скопировать из файла",
                                                              command=self.copy_from_file, position=[1020, 600],
                                                              background='#996633', width='25', height='3',
                                                              font="Sedan 12")
        self.active_elements['find_cost'] = create_label(font_color="#000000",
                                                                  text=f"Поиск по цене",
                                                                  position=[1000, 400], background="#996600",
                                                                  font="Sedan 14")
        self.active_elements['find_cost_combo'] = create_combo_box(width=12, font_color="#000000",
                                                                            position=[1000, 450],
                                                                            values=VALUE, default=None,
                                                                            callback=self.show_find_cost,
                                                                            font="Sedan 14")

    def show_menu(self):
        self.destroy_all()
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.show_main_screen,
                                                                 position=[1000, 700], background='#996633',
                                                                 width='25',
                                                                 height='3', font="Sedan 12")

        text = ""
        count = 1
        for dish in self.dishes:
            text = ''.join([text, f'\n{count}) ', dish.show_info()])
            count += 1
        if text == "":
            text += "Блюд пока нет"
        self.create_big_console(text)

    def show_find_cost(self, event):
        exp_radius = self.active_elements.get('find_cost_combo').get()
        text = f"Блюд с ценой {exp_radius}:"
        count = 1
        if exp_radius[0] == "0":
            start_exp = 0
        else:
            start_exp = int(exp_radius[:3])
        stop_exp = int(exp_radius[-3] + exp_radius[-2] + exp_radius[-1])
        for dish in self.dishes:
            if dish.cost in [i for i in range(start_exp, stop_exp + 1)]:
                text += f'\n{count}) {dish.get_full_name()}'
                count += 1
        if text == f"Блюд с ценой {exp_radius}:":
            text += "\nПо вашему запросу ничего не найдено"
        self.create_console(text)

    def copy_from_file(self):
        excel_data = pd.read_excel("data.xlsx")
        data = pd.DataFrame(excel_data, columns=['Название блюда', 'Тип блюда', 'Вес блюда', 'Цена блюда', 'Количество блюд'])
        dish_correct_flag = False
        dish_info, patient_info = [], []
        if len(data['Название блюда']) == len(data['Тип блюда']) == len(data['Вес блюда']) == len(data['Цена блюда']) == len(data['Количество блюд']):
            for index in range(len(data['Название блюда'])):
                if str(data['Название блюда'][index]) != 'nan':
                    name, name_flag = name_checker(data['Название блюда'][index])
                    type_of_food = data['Тип блюда'][index]
                    weight = data['Вес блюда'][index]
                    weight, weight_flag = weight_checker(str(weight))
                    cost = data['Цена блюда'][index]
                    cost, cost_flag = cost_checker(str(cost))
                    quantity = data['Количество блюд'][index]
                    quantity, quantity_flag = quantity_checker(str(quantity))
                    if type_of_food.lower().title() in TYPE_OF_FOOD:
                        type_of_food_flag = True
                    else:
                        type_of_food_flag = False
                    if not type_of_food_flag:
                        self.create_console(f'В строчке {index + 1} тип блюда введен неверно')
                    if not cost_flag:
                        self.create_console(f'В строчке {index + 1} цена блюда введена неверно')
                    if not name_flag:
                        self.create_console(f'В строчке {index + 1} название блюда введёна неверно')
                    if not quantity_flag:
                        self.create_console(f'В строчке {index + 1} количество блюд введёно неверно')
                    if not weight_flag:
                        self.create_console(f'В строчке {index + 1} вес блюда введён неверно')
                    if not cost_flag or not name_flag or not weight_flag or not quantity_flag or not type_of_food_flag:
                        break
                    find_equal = False
                    for dish in self.dishes:
                        if dish.type_of_food == type_of_food and dish.name == name and dish.cost == cost and dish.quantity == quantity and dish.weight == weight:
                            find_equal = True
                    for dish in dish_info:
                        if dish.type_of_food == type_of_food and dish.name == name and dish.cost == cost and dish.quantity == quantity and dish.weight == weight:
                            find_equal = True
                    if not find_equal:
                        dish_info.append(Dish(type_of_food=type_of_food, name=name, cost=cost, quantity=quantity, weight=weight))
            else:
                dish_correct_flag = True
        else:
            self.create_console('Количество записей про врачей не может быть однозначно установлено!')
        if dish_correct_flag:
            self.create_console('Записи из файла успешно добавлены')
            self.dishes.extend(dish_info)


    def add_order(self):
        self.create_console('Создана добавления заказа')
        self.destroy_all()
        OrderForm(self)

    def show_admin_auth(self):
        self.destroy_all()
        self.create_console('Переход на страницу входа в административную панель')
        self.active_elements['admin_label'] = create_label(font_color="#000000", text="Вход для\n Администратора",
                                                           position=[400, 72], background="#996600", font="Sedan 16")
        self.active_elements['admin_password_label'] = create_label(font_color="#000000", text="Введите пароль: ",
                                                                    position=[650, 590], background="#996600", font="Sedan 14")
        self.active_elements['admin_entry'] = create_entry(width=25, font="Sedan 14", font_color="#000000", position=[600, 630])
        self.active_elements['success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.check_correct_admin_password,
                                                        position=[600, 680], background='#996633', width='13', height='3', font="Sedan 12")
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Отменить", command=self.return_to_main_screen,
                                                        position=[750, 680],  background='#996633', width='13', height='3', font="Sedan 12")

    def destroy_all(self):
        for elem in self.active_elements:
            self.active_elements[elem].destroy()
        self.active_elements.clear()

    def return_to_main_screen(self):
        self.create_console('Возврат на основной экран')
        self.destroy_all()
        self.show_main_screen()

    def check_correct_admin_password(self):
        flag = check_correct_admin_password(self.active_elements['admin_entry'].get())
        if flag:
            self.destroy_all()
            AdminForm(self)
        else:
            self.create_console("Пароль введён неверно")

    def create_chose_dish(self, event):
        now_type_of_food = self.active_elements['combo_dish_auth_type_of_dish'].get()
        self.now_dishes = []
        for dish in self.dishes:
            if dish.type_of_food == now_type_of_food:
                self.now_dishes.append(dish)
        values = [self.now_dishes[dish].get_name(dish+1) for dish in range(len(self.now_dishes))]
        self.active_elements['combo_dish_auth_who'].destroy()
        self.active_elements['combo_dish_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 140], values=values, default=None, font="Sedan 14")

    def show_dishes(self):
        if not self.dish_auth_active:
            self.create_console('Создана форма добавления блюда')
            self.active_elements['dish_auth_label'] = create_label(font_color="#000000", text="Выберите тип блюда:",
                                                                   position=[300, 140], background="#996600", font="Sedan 14")
            self.active_elements['combo_dish_auth_type_of_dish'] = create_combo_box(width=12, font_color="#000000",
                                                                                    position=[500, 140], values=TYPE_OF_FOOD,
                                                                                    default=None, callback=self.create_chose_dish,
                                                                                    font="Sedan 14")
            self.active_elements['dish_auth_label_2'] = create_label(font_color="#000000", text="Выберите блюдо",
                                                                     position=[675, 140], background="#996600", font="Sedan 14")
            self.active_elements['combo_dish_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 140],
                                                                           values=[dish.get_name() for dish in self.now_dishes],
                                                                           default=None, font="Sedan 14")
            self.active_elements['dish_success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.enter_dish_menu, position=[1050, 140],
                                                                 background='#996633', width='13', height='1', font="Sedan 12")

            self.dish_auth_active = True
        else:
            self.create_console('Форма добавления доктора удалена')
            self.active_elements['dish_label'].destroy()
            self.active_elements['dish_auth_label'].destroy()
            self.active_elements['combo_dish_auth_type_of_dish'].destroy()
            self.active_elements['dish_auth_label_2'].destroy()
            self.active_elements['combo_dish_auth_who'].destroy()
            self.active_elements['dish_success'].destroy()
            self.active_elements.pop('dish_auth_label')
            self.active_elements.pop('combo_dish_auth_type_of_dish')
            self.active_elements.pop('dish_auth_label_2')
            self.active_elements.pop('combo_dish_auth_who')
            self.active_elements.pop('dish_success')
            self.active_elements.pop('dish_label')
            self.dish_auth_active = False
            self.now_dishes = []

    def show_all_orders(self):
        self.destroy_all()
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.show_main_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")

        text = ""
        count = 1
        for order in self.order:
            text = ''.join([text, f'\n{count}) ', order.show_info()])
            count += 1
        if text == "":
            text += "Заказов пока нет"
        self.create_big_console(text)


    def enter_dish_menu(self):
        if self.active_elements.get('combo_dish_auth_who').get() != "":
            dish_name = [self.now_dishes[dish].get_name(dish+1) for dish in range(len(self.now_dishes))]
            need_index = dish_name.index(self.active_elements['combo_dish_auth_who'].get())
            need_dish = self.now_dishes[need_index]
            DishForm(self, need_dish)
        else:
            self.create_console('Вы не выбрали блюдо')
