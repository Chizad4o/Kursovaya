from Help_elements import create_button, create_entry, create_label, create_combo_box
from constants import MAXTABLE, MAXQUANTITY
from checker import table_checker, quantity_checker_for_order
from .Order import Order


class OrderForm:
    def __init__(self, main):       #инизиализация экземпляров класса
        self.MainForm = main        #получение данных из main
        self.MainForm.window.title("Ресторан (Заказы)")         #Изменение названия окна
        self.show_main_screen()     #вызов метода показывания главное экрана формы заказа

    def show_main_screen(self):
        self.MainForm.active_elements['dish_help_label'] = create_label(font_color="#000000",
                                                                          text=f"Количество заказов в ресторане сейчас: {str(len(self.MainForm.order))}",
                                                                          position=[350, 0], background="#996600",
                                                                          font="Sedan 14")      #создание панели с надписью
        self.MainForm.active_elements['chose_what_do'] = create_label(font_color="#000000",
                                                                      text=f"Выберите действие:",
                                                                      position=[250, 600], background="#996600",
                                                                      font="Sedan 14")          #создание панели с надписью
        self.MainForm.active_elements['add_order'] = create_button(font_color='#ffffff',
                                                                    text="Добавить Заказ",
                                                                    command=self.add_order,
                                                                    position=[480, 600], background='#996633',
                                                                    width='25', height='3', font="Sedan 12")        #создание кнопки с вызовом метода add_order
        self.MainForm.active_elements['show_dishes'] = create_button(font_color='#ffffff',
                                                                      text="Показать заказы",
                                                                      command=self.show_all_orders,
                                                                      position=[740, 600], background='#996633',
                                                                      width='25', height='3', font="Sedan 12")      #создание кнопки с вызовом метода show_all_orders
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff',
                                                                 text="Вернуться на основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1150, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")                       #создание кнопки с вызовом метода MainForm.return_to_main_screen

    def return_to_order_screen(self):   #метод для возвращения на главную формы заказов
        self.MainForm.create_console('Возврат в панель заказов')
        self.MainForm.destroy_all()     #удаление всех элементов
        self.show_main_screen()         #показать главный экран

    def add_order(self):                #метод добавления заказа
        self.MainForm.destroy_all()     #уничтожить все элементы
        self.MainForm.create_console('Переход на страницу добавления заказа')
        self.Need_dishes = []           #создание/обнуление нужных блюд
        for dish in self.MainForm.dishes:   #для блюд, пока есть блюда добавлять в нужные блюда эти блюда
            self.Need_dishes.append(dish)
        values = [self.Need_dishes[dish].get_name() for dish in range(len(self.Need_dishes))]   #список для отображения всех блюд для формирования заказов
        self.MainForm.active_elements['dish_label'] = create_label(font_color="#000000",
                                                                     text="Страница добавления заказа",
                                                                     position=[400, 40], background="#996600",
                                                                     font="Sedan 14")           #создание панели с надписью
        self.MainForm.active_elements['number_of_table'] = create_label(font_color="#000000",
                                                                          text="Номер столика", position=[140, 150],
                                                                          background="#996600",
                                                                          font="Sedan 14")      #создание панели с надписью
        self.MainForm.active_elements['number_of_table_entry'] = create_entry(width=25, font_color="#000000",
                                                                                    position=[140, 200],
                                                                                    font="Sedan 14")    #создание панели для ввода
        self.MainForm.active_elements['dish1'] = create_label(font_color="#000000",
                                                                    text="Блюдо 1", position=[140, 250],
                                                                    background="#996600",
                                                                    font="Sedan 14")            #создание панели с надписью
        self.MainForm.active_elements['dish1_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 300],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)    #создание поля с выбором, список состоит из всех блюд в меню
        self.MainForm.active_elements['quantity'] = create_label(font_color="#000000",
                                                              text="Кол-во", position=[50, 250],
                                                              background="#996600",
                                                              font="Sedan 14")                  #создание панели с надписью
        self.MainForm.active_elements['quantity1_entry'] = create_entry(width=5, font_color="#000000",
                                                                                    position=[50, 300],
                                                                                    font="Sedan 14")    #создание панели для ввода
        self.MainForm.active_elements['dish2'] = create_label(font_color="#000000",text="Блюдо 2",
                                                                position=[140, 350], background="#996600",
                                                                font="Sedan 14")                #создание панели с надписью
        self.MainForm.active_elements['dish2_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 400],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)    #создание поля с выбором, список состоит из всех блюд в меню
        self.MainForm.active_elements['quantity2_entry'] = create_entry(width=5, font_color="#000000",
                                                                        position=[50, 400],
                                                                        font="Sedan 14")        #создание панели для ввода
        self.MainForm.active_elements['dish3'] = create_label(font_color="#000000",
                                                                    text="Блюдо 3", position=[140, 450],
                                                                    background="#996600",
                                                                    font="Sedan 14")            #создание панели с надписью
        self.MainForm.active_elements['dish3_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 500],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)    #создание поля с выбором, список состоит из всех блюд в меню
        self.MainForm.active_elements['quantity3_entry'] = create_entry(width=5, font_color="#000000",
                                                                        position=[50, 500],
                                                                        font="Sedan 14")
        self.MainForm.active_elements['dish4'] = create_label(font_color="#000000",
                                                                          text="Блюдо 4", position=[140, 550],
                                                                          background="#996600",
                                                                          font="Sedan 14")      #создание панели с надписью
        self.MainForm.active_elements['dish4_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 600],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)    #создание поля с выбором, список состоит из всех блюд в меню
        self.MainForm.active_elements['quantity4_entry'] = create_entry(width=5, font_color="#000000",
                                                                        position=[50, 600],
                                                                        font="Sedan 14")        #создание панели для ввода
        self.MainForm.active_elements['dish5'] = create_label(font_color="#000000",
                                                                  text="Блюдо 5", position=[140, 650],
                                                                  background="#996600",
                                                                  font="Sedan 14")              #создание панели с надписью
        self.MainForm.active_elements['dish5_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 700],
                                                                              values=values,
                                                                              font="Sedan 14", default=None)    #создание поля с выбором, список состоит из всех блюд в меню
        self.MainForm.active_elements['quantity5_entry'] = create_entry(width=5, font_color="#000000",
                                                                        position=[50, 700],
                                                                        font="Sedan 14")        #создание панели для ввода
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_order_screen,
                                                                 position=[1000, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")       #создание кнопки с вызовом метода return_to_order_screen
        self.MainForm.active_elements['complete'] = create_button(font_color='#ffffff', text="Выполнить",
                                                                  command=self.add_new_order, position=[190, 750],
                                                                  background='#996633', width=20, height='3',
                                                                  font="Sedan 12")                  #создание кнопки с вызовом метода add_new_order

    def add_new_order(self):        #метод для подтверждения нового заказа
        table_number, table_number_flag = table_checker(self.MainForm.active_elements['number_of_table_entry'].get())   #Получаем значение с нужного нам элемента и проходим через проверку
        dish1 = self.MainForm.active_elements['dish1_entry'].get()      #Получаем значение с нужного нам элемента
        dish2 = self.MainForm.active_elements['dish2_entry'].get()      #Получаем значение с нужного нам элемента
        dish3 = self.MainForm.active_elements['dish3_entry'].get()      #Получаем значение с нужного нам элемента
        dish4 = self.MainForm.active_elements['dish4_entry'].get()      #Получаем значение с нужного нам элемента
        dish5 = self.MainForm.active_elements['dish5_entry'].get()      #Получаем значение с нужного нам элемента
        quantity1, quantity1_flag = quantity_checker_for_order(self.MainForm.active_elements['quantity1_entry'].get())  #Получаем значение с нужного нам элемента и проходим через проверку
        quantity2, quantity2_flag = quantity_checker_for_order(self.MainForm.active_elements['quantity2_entry'].get())  #Получаем значение с нужного нам элемента и проходим через проверку
        quantity3, quantity3_flag = quantity_checker_for_order(self.MainForm.active_elements['quantity3_entry'].get())  #Получаем значение с нужного нам элемента и проходим через проверку
        quantity4, quantity4_flag = quantity_checker_for_order(self.MainForm.active_elements['quantity4_entry'].get())  #Получаем значение с нужного нам элемента и проходим через проверку
        quantity5, quantity5_flag = quantity_checker_for_order(self.MainForm.active_elements['quantity5_entry'].get())  #Получаем значение с нужного нам элемента и проходим через проверку
        dish1_flag = True               #
        dish2_flag = True               #
        dish3_flag = True               #Флаги о корректности ввода блюда, возможна нехватка блюд
        dish4_flag = True               #
        dish5_flag = True               #
        sum_cost = 0                    #суммарная стоимость заказа
        if not table_number_flag:       #если не флаг, то столик выбран не правильно
            self.MainForm.create_console(
                f"Номер столика введен неверно\n Учтите что максимально количество \nстоликов не может быть более {MAXTABLE}\nи не меньше нуля")
        if not quantity1_flag:          #если не флаг, то количество выбрано не правильно
            self.MainForm.create_console(
                f"Количество блюд введено неверно\n Должно быть введено число не более чем {MAXQUANTITY}\nи не меньше нуля")
        if not quantity2_flag:          #если не флаг, то количество выбрано не правильно
            self.MainForm.create_console(
                f"Количество блюд введено неверно\n Должно быть введено число не более чем {MAXQUANTITY}\nи не меньше нуля")
        if not quantity3_flag:          #если не флаг, то количество выбрано не правильно
            self.MainForm.create_console(
                f"Количество блюд введено неверно\n Должно быть введено число не более чем {MAXQUANTITY}\nи не меньше нуля")
        if not quantity4_flag:          #если не флаг, то количество выбрано не правильно
            self.MainForm.create_console(
                f"Количество блюд введено неверно\n Должно быть введено число не более чем {MAXQUANTITY}\nи не меньше нуля")
        if not quantity5_flag:          #если не флаг, то количество выбрано не правильно
            self.MainForm.create_console(
                f"Количество блюд введено неверно\n Должно быть введено число не более чем {MAXQUANTITY}\nи не меньше нуля")
        if table_number_flag and quantity1_flag and quantity2_flag and quantity3_flag and quantity4_flag and quantity5_flag:              #если флаг, то все верно
            for i in range (5):                 #в цикле до 5 элементов
                now_food = self.MainForm.active_elements[f'dish{i+1}_entry'].get()              #нынешнее блюдо получаем из нужного активного элемента
                now_quantity = self.MainForm.active_elements[f'quantity{i+1}_entry'].get()      #нынешнее количество блюд получаем из нужного активного элемента
                for dish in self.MainForm.dishes:               #пока есть блюда сравниваем
                    if dish.name == now_food:                   #если имя совпадает из меню и блюда в заказе, то
                        if int(now_quantity) > dish.quantity:       #если количество заказанных превышает кол-во оставшихся блюд, то
                            if i == 0:                                  #если цикл в первой итерации, то ошибка в блюде один
                                dish1_left = dish.quantity              #кол-во оставшихся получаем из dish.quantity
                                dish1_flag = False                      #меняем flag на False
                            elif i == 1:                                #если цикл во второй итерации, то ошибка в блюде два
                                dish2_left = dish.quantity              #кол-во оставшихся получаем из dish.quantity
                                dish2_flag = False                      #меняем flag на False
                            elif i == 2:                                #если цикл в третьей итерации, то ошибка в блюде тр
                                dish3_left = dish.quantity              #кол-во оставшихся получаем из dish.quantity
                                dish3_flag = False                      #меняем flag на False
                            elif i == 3:                                #если цикл в четвертой итерации, то ошибка в блюде четыре
                                dish4_left = dish.quantity              #кол-во оставшихся получаем из dish.quantity
                                dish4_flag = False                      #меняем flag на False
                            elif i == 4:                                #если цикл в пятой итерации, то ошибка в блюде пять
                                dish5_left = dish.quantity              #кол-во оставшихся получаем из dish.quantity
                                dish5_flag = False                      #меняем flag на False
                        else:       #иначе
                            dish.quantity = int(dish.quantity) - int(now_quantity)  #уменьшаем кол-во данных блюд
                            sum_cost += int(dish.cost)*int(now_quantity)            #и увеличиваем сумму заказа равную произведению цены на кол-во
                if now_quantity == '':      #если сейчас в элементе кол-во пустое, то обнуляем эту переменную, так же по итерациям
                    if i == 0:
                        quantity1 = ''
                    elif i == 1:
                        quantity2 = ''
                    elif i == 2:
                        quantity3 = ''
                    elif i == 3:
                        quantity4 = ''
                    elif i == 4:
                        quantity5 = ''
                else: #иначе
                    SHT = 'шт.'     #объявляю переменнуб SHT с текстом Шт. который буду добавлять к концу строки, если есть какое-либо значение, также по итерациям
                    if i == 0:
                        quantity1 = str(quantity1)
                        quantity1 += SHT
                    elif i == 1:
                        quantity2 = str(quantity2)
                        quantity2 += SHT
                    elif i == 2:
                        quantity3 = str(quantity3)
                        quantity3 += SHT
                    elif i == 3:
                        quantity4 = str(quantity4)
                        quantity4 += SHT
                    elif i == 4:
                        quantity5 = str(quantity5)
                        quantity5 += SHT
                if not dish1_flag:  #если не флаг блюда 1, то ошибка формирования заказа из-за блюда 1
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо {dish1},\n осталось {dish1_left}')
                if not dish2_flag:  #если не флаг блюда 2, то ошибка формирования заказа из-за блюда 2
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо {dish2},\n осталось {dish2_left}')
                if not dish3_flag:  #если не флаг блюда 3, то ошибка формирования заказа из-за блюда 3
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо {dish3},\n осталось {dish3_left}')
                if not dish4_flag:  #если не флаг блюда 4, то ошибка формирования заказа из-за блюда 4
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо {dish4},\n осталось {dish4_left}')
                if not dish5_flag:  #если не флаг блюда 5, то ошибка формирования заказа из-за блюда 5
                    self.MainForm.create_console(
                        f'Заказ не может быть сформирован, \nтак как кончилось блюдо {dish5},\n осталось {dish5_left}')
            if dish1_flag and dish2_flag and dish3_flag and dish4_flag and dish5_flag:  #если все флаги true, то переносим значения в Order
                self.MainForm.order.append(
                    Order(table_number=table_number, dish1=dish1,  dish2=dish2, dish3=dish3, dish4=dish4, dish5=dish5, sum_cost=sum_cost,
                          quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, quantity5=quantity5))
                self.return_to_order_screen()


    def show_all_orders(self):                  #метод для отображения всех заказов
        self.MainForm.destroy_all()             #удаляем все элементы
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_order_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")       #создание кнопки с вызовом метода return_to_order_screen
        text = ""                               #объявление переменной
        count = 1                               #объявление переменной
        for order in self.MainForm.order:       #для order пока есть заказы
            text = ''.join([text, f'\n{count}) ', order.show_info()])       #добавление в текст кол-во блюд и всей информации о блюде
            count += 1                          #обновление переменной
        if text == "":                          #если текст не изменился, то заказов нет
            text += "Заказов пока нет"
        self.MainForm.create_big_console(text)  #вызываем окно(консоль) в которую выводим text
