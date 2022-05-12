from Help_elements import create_button, create_entry, create_label, create_combo_box
from constants import MAXLENNAME, MAXTABLEVALUE
from checker import table_checker
from .Order import Order


class OrderForm:
    def __init__(self, main):
        self.MainForm = main
        self.MainForm.window.title("Ресторан (администратор)")
        self.MainForm.create_console('Переход на панель администратора')
        self.show_main_screen()

    def show_main_screen(self):
        self.MainForm.active_elements['dish_help_label'] = create_label(font_color="#000000",
                                                                          text=f"Количество заказов в ресторане сейчас: {str(len(self.MainForm.order))}",
                                                                          position=[400, 80], background="#996600",
                                                                          font="Sedan 14")
        self.MainForm.active_elements['chose_what_do'] = create_label(font_color="#000000",
                                                                      text=f"Выберите действие:",
                                                                      position=[250, 600], background="#996600",
                                                                      font="Sedan 14")
        self.MainForm.active_elements['add_order'] = create_button(font_color='#ffffff',
                                                                    text="Добавить Заказ",
                                                                    command=self.add_order,
                                                                    position=[480, 600], background='#996633',
                                                                    width='25', height='3', font="Sedan 12")
        self.MainForm.active_elements['show_dishes'] = create_button(font_color='#ffffff',
                                                                      text="Показать заказы",
                                                                      command=self.show_all_orders,
                                                                      position=[740, 600], background='#996633',
                                                                      width='25', height='3', font="Sedan 12")
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff',
                                                                 text="Вернуться на основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1150, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")

    def return_to_order_screen(self):
        self.MainForm.create_console('Возврат в панель администратора')
        self.MainForm.destroy_all()
        self.show_main_screen()

    def add_order(self):
        self.MainForm.destroy_all()
        self.MainForm.create_console('Переход на страницу добавления заказа')
        self.Need_dishes = []
        for dish in self.MainForm.dishes:
            self.Need_dishes.append(dish)
        values = [self.Need_dishes[dish].get_name() for dish in range(len(self.Need_dishes))]
        self.MainForm.active_elements['dish_label'] = create_label(font_color="#000000",
                                                                     text="Страница добавления заказа",
                                                                     position=[400, 40], background="#996600",
                                                                     font="Sedan 14")
        self.MainForm.active_elements['number_of_table'] = create_label(font_color="#000000",
                                                                          text="Номер столика", position=[140, 150],
                                                                          background="#996600",
                                                                          font="Sedan 14")
        self.MainForm.active_elements['number_of_table_entry'] = create_entry(width=25, font_color="#000000",
                                                                                    position=[140, 200],
                                                                                    font="Sedan 14")
        self.MainForm.active_elements['dish1'] = create_label(font_color="#000000",
                                                                    text="Блюдо 1", position=[140, 250],
                                                                    background="#996600",
                                                                    font="Sedan 14")
        self.MainForm.active_elements['dish1_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 300],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['dish2'] = create_label(font_color="#000000",text="Блюдо 2",
                                                                position=[140, 350], background="#996600",
                                                                font="Sedan 14")
        self.MainForm.active_elements['dish2_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 400],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['dish3'] = create_label(font_color="#000000",
                                                                    text="Блюдо 3", position=[140, 450],
                                                                    background="#996600",
                                                                    font="Sedan 14")

        self.MainForm.active_elements['dish3_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 500],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['dish4'] = create_label(font_color="#000000",
                                                                          text="Блюдо 4", position=[140, 550],
                                                                          background="#996600",
                                                                          font="Sedan 14")
        self.MainForm.active_elements['dish4_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 600],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['dish5'] = create_label(font_color="#000000",
                                                                  text="Блюдо 5", position=[140, 650],
                                                                  background="#996600",
                                                                  font="Sedan 14")
        self.MainForm.active_elements['dish5_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 700],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_order_screen,
                                                                 position=[1000, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")
        self.MainForm.active_elements['complete'] = create_button(font_color='#ffffff', text="Выполнить",
                                                                  command=self.add_new_order, position=[190, 750],
                                                                  background='#996633', width=20, height='3',
                                                                  font="Sedan 12")

    def add_new_order(self):
        table_number, table_number_flag = table_checker(self.MainForm.active_elements['number_of_table_entry'].get())
        dish1 = self.MainForm.active_elements['dish1_entry'].get()
        dish2 = self.MainForm.active_elements['dish2_entry'].get()
        dish3 = self.MainForm.active_elements['dish3_entry'].get()
        dish4 = self.MainForm.active_elements['dish4_entry'].get()
        dish5 = self.MainForm.active_elements['dish5_entry'].get()
        dish1_flag = True
        dish2_flag = True
        dish3_flag = True
        dish4_flag = True
        dish5_flag = True
        sum_cost = 0
        if not table_number_flag:
            self.MainForm.create_console(
                f"Номер столика введен неверно\n Учтите что максимально количество столиков не может быть более {MAXTABLEVALUE}\nи не меньше нуля")
        if table_number_flag:
            for i in range (5):
                now_food = self.MainForm.active_elements[f'dish{i+1}_entry'].get()
                for dish in self.MainForm.dishes:
                    if dish.name == now_food:
                        if dish.quantity == 0:
                            if i == 0:
                                dish1_flag = False
                            elif i == 1:
                                dish2_flag = False
                            elif i == 2:
                                dish3_flag = False
                            elif i == 3:
                                dish4_flag = False
                            elif i == 4:
                                dish5_flag = False
                        else:
                            dish.quantity = int(dish.quantity) - 1
                            sum_cost += int(dish.cost)
                if not dish1_flag:
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо 1')
                if not dish2_flag:
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо 2')
                if not dish3_flag:
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо 3')
                if not dish4_flag:
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо 4')
                if not dish5_flag:
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо 5')
            if dish1_flag and dish2_flag and dish3_flag and dish4_flag and dish5_flag:
                self.MainForm.order.append(
                    Order(table_number=table_number, dish1=dish1,  dish2=dish2, dish3=dish3, dish4=dish4, dish5=dish5, sum_cost=sum_cost))
                self.return_to_order_screen()


    def show_all_orders(self):
        self.MainForm.destroy_all()
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_order_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")

        text = ""
        count = 1
        for order in self.MainForm.order:
            text = ''.join([text, f'\n{count}) ', order.show_info()])
            count += 1
        if text == "":
            text += "Заказов пока нет"
        self.MainForm.create_big_console(text)
