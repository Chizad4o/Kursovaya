import tkinter as tk                    #Импорт библиотеки для создания форм, функциональных клавиш
from Help_elements import create_button, create_entry, create_label, create_combo_box           #Импорт вспомогательных элементов
from checker import check_correct_admin_password, name_checker, cost_checker, quantity_checker, weight_checker      #Импорт методов проверки
from .AdminForm import AdminForm        #импорт формы, для будущего обращения к нему
from .DishForm import DishForm          #импорт формы, для будущего обращения к нему
from .OrderForm import OrderForm        #импорт формы, для будущего обращения к нему
from constants import TYPE_OF_FOOD, VALUE       #Импорт постоянных значений
import os                   #допуск программы к работе с файлом
import pandas as pd         #импорт библиотеки для работы с таблицой excel
from .Dish import Dish      #Импорт класса Dish


class MainForm:
    def __init__(self):     #инизиализация экземпляров класса
        self.dish_auth_active = None        #флаг аутентификации для блюда
        self.dishes, self.order, self.patients = [], [], [] #обнуление переменных
        self.active_elements = {}           #обнуляем активные элементы
        self.window = tk.Tk()               #создание окна
        self.window.geometry('1400x875')    #создание окна с заднными размерами

        background = tk.PhotoImage(file=os.path.abspath(os.path.join('background.png')))        #объявление переменной, которая берет фотографию для внешнего вида окна
        self.__background_label = tk.Label(self.window, image=background)               #Вставка фотографии в окно программы
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)                #Расположение фотографии на фоне

        label_name = tk.PhotoImage(file=os.path.abspath(os.path.join('label.png')))              #объявление переменной, которая берет фотографию для внешнего вида окна
        self.__secret_label = tk.Label(self.window, image=label_name, background='#996633')     #Вставка фотографии в окно программы
        self.__secret_label.place(x=1, y=1)                             #Расположение лейбла

        self.show_main_screen()             #вызов метода для показывания главного экрана
        self.create_console()               #вызов метода для создания внутреннего окна(консоли)
        self.window.mainloop()              #запуск цикла библиотеки Tkinter

    def create_console(self, text=""):      #метод для создания консоли
        label = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=50,
            height=16,
        )
        label.place(x=440, y=225)           #расположение

    def create_big_console(self, text=""):      #метод для создания консоли большого размера
        self.active_elements['big_console'] = tk.Label(
            text=text,
            font="Sedan 14",
            foreground='#000000',
            background='#ffffff',
            width=100,
            height=22,
        )
        self.active_elements['big_console'].place(x=150, y=200)

    def show_main_screen(self):     #метод для отображения главной формы(формы)
        self.destroy_all()          #метод для уничтожения всех элементов
        self.window.title("Ресторан")           #Изменение названия окна
        self.active_elements['chose_what_do'] = create_label(font_color='#000000', text="Выберите действие:",
                                                             position=[250, 700], background="#996600", font="Sedan 14")        #создание окошка с надписью
        self.active_elements['admin_button'] = create_button(font_color='#ffffff', text="Войти как админ",
                                                             command=self.show_admin_auth, position=[240, 600],
                                                             background='#996633', width='25',
                                                             height='3', font="Sedan 12")               #создание кнопки, которая вызывает метод show_admin_auth
        self.dish_auth_active = False           #меняем флаг аутентификации для блюда
        self.now_dishes = []                    #Обнуляем переменные now_dishes
        self.now_orders = []                    #Обнуляем переменные now_orders
        self.active_elements['dish_button'] = create_button(font_color='#ffffff', text="Поиск/Удаление блюда",
                                                            command=self.show_dishes, position=[500, 600],
                                                            background='#996633', width='25',
                                                            height='3', font="Sedan 12")    #создание кнопки, которая вызывает метод show_dishes
        self.patient_auth_active = False
        self.active_elements['new_order_button'] = create_button(font_color='#ffffff', text="Добавить заказ",
                                                                 command=self.add_order, position=[760, 600],
                                                                 background='#996633', width='25',
                                                                 height='3', font="Sedan 12")   #создание кнопки, которая вызывает метод add_order
        self.active_elements['order_show_button'] = create_button(font_color='#ffffff', text="Заказы",
                                                                  command=self.show_all_orders, position=[760, 700],
                                                                  background='#996633', width='25',
                                                                  height='3', font="Sedan 12")  #создание кнопки, которая вызывает метод show_all_orders
        self.active_elements['show_menu'] = create_button(font_color='#ffffff', text="Меню",
                                                                 command=self.show_menu, position=[500, 700],
                                                                 background='#996633', width='25', height='3',
                                                                 font="Sedan 12")   #создание кнопки, которая вызывает метод show_menu
        self.file_flag = False
        self.active_elements['copy_file_btn'] = create_button(font_color='#ffffff', text="Скопировать из файла",
                                                              command=self.copy_from_file, position=[1020, 600],
                                                              background='#996633', width='25', height='3',
                                                              font="Sedan 12")  #создание кнопки, которая вызывает метод copy_from_file
        self.active_elements['find_cost'] = create_label(font_color="#000000",
                                                                  text=f"Поиск по цене",
                                                                  position=[1000, 400], background="#996600",
                                                                  font="Sedan 14")                  #создание окошка с надписью
        self.active_elements['find_cost_combo'] = create_combo_box(width=12, font_color="#000000",
                                                                            position=[1000, 450],
                                                                            values=VALUE, default=None,
                                                                            callback=self.show_find_cost,
                                                                            font="Sedan 14")        #создание поля с выбором и вызывает метод show_find_cost

    def show_menu(self):        #Метод для вывода меню
        self.destroy_all()              #уничтожить все элементы
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.show_main_screen,
                                                                 position=[1000, 700], background='#996633',
                                                                 width='25',
                                                                 height='3', font="Sedan 12")   #создание кнопки, которая вызывает метод show_main_screen

        text = ""          #объявление переменной
        count = 1       #объявление переменной
        for dish in self.dishes:            #для dish пока есть блюда
            text = ''.join([text, f'\n{count}) ', dish.show_info()])        #добавление в текст кол-во блюд и всей информации о блюде
            count += 1          #обновление переменной
        if text == "":      #если текст не изменился, то блюд нет
            text += "Блюд пока нет"
        self.create_big_console(text)       #вызываем окно(консоль) в которую выводим text

    def show_find_cost(self, event):    #Метод для поиска по цене
        exp_radius = self.active_elements.get('find_cost_combo').get()      #получаем значение с поля с выбором
        text = f"Блюд с ценой {exp_radius}:"                                #передаем значение переменной text, где exp_radius это диапазон поиска
        count = 1                                                           #приравниваем количество к 1
        if exp_radius[0] == "0":                                            #если первое значение в диапазоне 0, то...
            start_exp = 0                                                   #начальное значение 0
        else:                                                               #иначе
            start_exp = int(exp_radius[:3])                                 #начальное значение сравнения это первые 3 элемента строки, которые конвертируем в int
        stop_exp = int(exp_radius[-3] + exp_radius[-2] + exp_radius[-1])    #конечное значение диапазона это сумма последних 3 элементов строки, которые в последствии конверитруются в int
        for dish in self.dishes:                                            #для dish в диапазоне, пока есть блюда
            if dish.cost in [i for i in range(start_exp, stop_exp + 1)]:    #если цена в выбранном диапазоне, то...
                text += f'\n{count}) {dish.get_full_name()}'                #обновляем переменную text, в которую записываем количество попаданий и название блюда с ценой и типом блюда
                count += 1                                                  #обновляем счетчик количества блюд с определнной ценой
        if text == f"Блюд с ценой {exp_radius}:":                           #если текст не изменился, то...
            text += "\nПо вашему запросу ничего не найдено"                 #обновляем переменную text
        self.create_console(text)                                           #вызываем окно(консоль) в которую выводим text

    def copy_from_file(self):           #Метод для копирования из файла
        excel_data = pd.read_excel("data.xlsx")             #Данные excel получаем из таблицы
        data = pd.DataFrame(excel_data, columns=['Название блюда', 'Тип блюда', 'Вес блюда', 'Цена блюда', 'Количество блюд'])  #данные по колоннам
        dish_correct_flag = False                           #флаг для корректного ввода
        dish_info, patient_info = [], []                    #обнуляем переменные
        if len(data['Название блюда']) == len(data['Тип блюда']) == len(data['Вес блюда']) == len(data['Цена блюда']) == len(data['Количество блюд']):      #если кол-во строк совпадает, то
            for index in range(len(data['Название блюда'])):                            #для индекса в диапазоне строк получаем значения
                if str(data['Название блюда'][index]) != 'nan':                         #если значение строки не nan, то
                    name, name_flag = name_checker(data['Название блюда'][index])       #получаем значение из нужной ячейки пропуская через проверку
                    type_of_food = data['Тип блюда'][index]                             #получаем значение из нужной ячейки пропуская через проверку
                    weight = data['Вес блюда'][index]                                   #получаем значение из нужной ячейки пропуская через проверку
                    weight, weight_flag = weight_checker(str(weight))                   #получаем значение из нужной ячейки пропуская через проверку
                    cost = data['Цена блюда'][index]                                    #получаем значение из нужной ячейки пропуская через проверку
                    cost, cost_flag = cost_checker(str(cost))                           #получаем значение из нужной ячейки пропуская через проверку
                    quantity = data['Количество блюд'][index]                           #получаем значение из нужной ячейки пропуская через проверку
                    quantity, quantity_flag = quantity_checker(str(quantity))           #получаем значение из нужной ячейки пропуская через проверку
                    if type_of_food.lower().title() in TYPE_OF_FOOD:                    #Если тип блюда подходит постоянной, то
                        type_of_food_flag = True                                        #Флаг True
                    else:                                                               #Иначе
                        type_of_food_flag = False                                       #Флаг False
                    if not type_of_food_flag:       #если не флаг типа блюда, то выводим ошибку о вводе данных
                        self.create_console(f'В строчке {index + 1} тип блюда введен неверно')
                    if not cost_flag:               #если не флаг цены блюда, то выводим ошибку о вводе данных
                        self.create_console(f'В строчке {index + 1} цена блюда введена неверно')
                    if not name_flag:               #если не флаг названия блюда, то выводим ошибку о вводе данных
                        self.create_console(f'В строчке {index + 1} название блюда введёна неверно')
                    if not quantity_flag:           #если не флаг количества блюд, то выводим ошибку о вводе данных
                        self.create_console(f'В строчке {index + 1} количество блюд введёно неверно')
                    if not weight_flag:             #если не флаг веса блюда, то выводим ошибку о вводе данных
                        self.create_console(f'В строчке {index + 1} вес блюда введён неверно')
                    if not cost_flag or not name_flag or not weight_flag or not quantity_flag or not type_of_food_flag:     #если один НЕ флаг, то прырваем цикл
                        break
                    find_equal = False              #поиск такой же False
                    for dish in self.dishes:        #для dish пока есть блюда
                        if dish.type_of_food == type_of_food and dish.name == name and dish.cost == cost and dish.quantity == quantity and dish.weight == weight:   #если значения с dish совпадают, то нашли такое же блюдо
                            find_equal = True       #меняем флаг на True
                    for dish in dish_info:          #для dish по dish_info
                        if dish.type_of_food == type_of_food and dish.name == name and dish.cost == cost and dish.quantity == quantity and dish.weight == weight:   #если значения с dish совпадают, то нашли такое же блюдо
                            find_equal = True       #меняем флаг на True
                    if not find_equal:              #если не нашли такое же блюдо, то вводим значения в конец dish_info
                        dish_info.append(Dish(type_of_food=type_of_food, name=name, cost=cost, quantity=quantity, weight=weight))
            else:           #иначе
                dish_correct_flag = True            #флаг ввода блюда меняем на true
        else:       #иначе мы не можем установить однозначно блюда
            self.create_console('Количество записей про блюда не может быть однозначно установлено!')      #
        if dish_correct_flag:       #если флаг ввода блюда, то блюда введены успешно
            self.create_console('Записи из файла успешно добавлены')
            self.dishes.extend(dish_info)       #добавляем в dishes полученные блюда


    def add_order(self):        #метод добавления заказа
        self.create_console('Создана форма добавления заказа')    #Вывод информации о переходе на окно заказов
        self.destroy_all()                                  #уничтожить все элементы
        OrderForm(self)                                     #вызоы формы

    def show_admin_auth(self):  #метод для ввода пароля, который нужен для перехода в админ
        self.destroy_all()      #уничтожить все элементы
        self.create_console('Переход на страницу входа в административную панель')
        self.active_elements['admin_label'] = create_label(font_color="#000000", text="Вход для\n Администратора",
                                                           position=[400, 72], background="#996600", font="Sedan 16")               #создание окошка с надписью
        self.active_elements['admin_password_label'] = create_label(font_color="#000000", text="Введите пароль: ",
                                                                    position=[650, 590], background="#996600", font="Sedan 14")     #создание окошка с надписью
        self.active_elements['admin_entry'] = create_entry(width=25, font="Sedan 14", font_color="#000000", position=[600, 630])
        self.active_elements['success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.check_correct_admin_password,
                                                        position=[600, 680], background='#996633', width='13', height='3', font="Sedan 12") #создание кнопки, которая вызывает метод check_correct_admin_password
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Отменить", command=self.return_to_main_screen,
                                                        position=[750, 680],  background='#996633', width='13', height='3', font="Sedan 12")    #создание кнопки, которая вызывает метод return_to_main_screen

    def destroy_all(self):              #метод уничтожения всех элементов
        for elem in self.active_elements:   #для элементов пока есть активные элементы на экране
            self.active_elements[elem].destroy()    #удалить этот элемент
        self.active_elements.clear()

    def return_to_main_screen(self):    #метод возвращения на основной экран
        self.create_console('Возврат на основной экран')
        self.destroy_all()          #уничтожения всех элементов
        self.show_main_screen()     #возвращение на главный экран

    def check_correct_admin_password(self):     #метод для проверки пароля
        flag = check_correct_admin_password(self.active_elements['admin_entry'].get())      #флаг проверки пароля, который получает значение с проверки
        if flag:        #Если флаг, то...
            self.destroy_all()      #Уничтожаем все элементы
            AdminForm(self)         #Переход в форму админа
        else:           #иначе
            self.create_console("Пароль введён неверно")    #пароль введен неверно

    def create_chose_dish(self, event):                     #метод создания перечня блюд, которые удовлетворяют выбранному типу блюда
        now_type_of_food = self.active_elements['combo_dish_auth_type_of_dish'].get()       #выбранный тип блюда получает из активного элемента
        self.now_dishes = []                    #создаем переменную блюда, которые будут выводится
        for dish in self.dishes:                #для блюд пока есть блюда
            if dish.type_of_food == now_type_of_food:   #если блюдо удовлетворяет этому типу блюда, то добавляем в список блюд, которые будут появляться
                self.now_dishes.append(dish)
        values = [self.now_dishes[dish].get_name(dish+1) for dish in range(len(self.now_dishes))]       #переменная для поля с выбором
        self.active_elements['combo_dish_auth_who'].destroy()           #уничтожаем элемент combo_dish_auth_who, чтобы его заменить
        self.active_elements['combo_dish_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 180], values=values, default=None, font="Sedan 14")

    def show_dishes(self):          #метод для поиска блюда
        if not self.dish_auth_active:       #если аутентификация блюда не активна, то создаем нужные нам кнопки
            self.create_console('Создана форма добавления блюда')
            self.active_elements['dish_auth_label'] = create_label(font_color="#000000", text="Выберите тип блюда:",
                                                                   position=[300, 180], background="#996600", font="Sedan 14")          #создание окошка с надписью
            self.active_elements['combo_dish_auth_type_of_dish'] = create_combo_box(width=12, font_color="#000000",
                                                                                    position=[500, 180], values=TYPE_OF_FOOD,
                                                                                    default=None, callback=self.create_chose_dish,
                                                                                    font="Sedan 14")                                    #создание поля с выбором типа блюда и последующим вызовом метода create_chose_dish
            self.active_elements['dish_auth_label_2'] = create_label(font_color="#000000", text="Выберите блюдо",
                                                                     position=[675, 180], background="#996600", font="Sedan 14")        #создание окошка с надписью
            self.active_elements['combo_dish_auth_who'] = create_combo_box(width=12, font_color="#000000", position=[875, 180],
                                                                           values=[dish.get_name() for dish in self.now_dishes],
                                                                           default=None, font="Sedan 14")                               #создание поля с выбором из списка, который составлен в методе create_chose_dish
            self.active_elements['dish_success'] = create_button(font_color='#ffffff', text="Выполнить", command=self.enter_dish_menu, position=[1050, 180],
                                                                 background='#996633', width='13', height='1', font="Sedan 12") #создание кнопки, которая вызывает метод enter_dish_menu

            self.dish_auth_active = True            #меняем флаг на True
        else:       #иначе
            self.create_console('Форма блюда удалена')      #удаляем активные в этом же методе элементы
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
            self.dish_auth_active = False                   #меняем flag на False
            self.now_dishes = []                            #обнуляем переменную

    def show_all_orders(self):      #метод показывания всех заказов
        self.destroy_all()          #удаляем все элементы
        self.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.show_main_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")   #создание кнопки, которая вызывает метод show_main_screen

        text = ""                       #объявление переменной
        count = 1                       #объявление переменной
        for order in self.order:        #для order пока есть заказы
            text = ''.join([text, f'\n{count}) ', order.show_info()])    #добавление в текст кол-во блюд и всей информации о блюде
            count += 1                  #обновление переменной
        if text == "":                  #если текст не изменился, то заказов нет
            text += "Заказов пока нет"
        self.create_big_console(text)   #вызываем окно(консоль) в которую выводим text


    def enter_dish_menu(self):          #метод для перехода в форму блюда
        if self.active_elements.get('combo_dish_auth_who').get() != "":     #если из полученного элемента не пустое значение, то
            dish_name = [self.now_dishes[dish].get_name(dish+1) for dish in range(len(self.now_dishes))]        #название блюда получаем из диапазона нужных блюд
            need_index = dish_name.index(self.active_elements['combo_dish_auth_who'].get())                     #нужный индекс равен индексу из поля с выбором названия
            need_dish = self.now_dishes[need_index]                                                             #нужное блюдо равно блюду сейчас с ныжным индексом
            DishForm(self, need_dish)                                                                           #вызов формы с передачей нужно блюда
        else:           #иначе
            self.create_console('Вы не выбрали блюдо')      #вы не выбрали блюдо
