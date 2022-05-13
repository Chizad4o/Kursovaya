from Help_elements import create_button, create_entry, create_label, create_combo_box
from constants import MAXCOST, MAXLENNAME, VALUE, TYPE_OF_FOOD, MAXWEIGHT, MAXQUANTITY
from checker import name_checker, cost_checker, quantity_checker, weight_checker
from .Dish import Dish


class AdminForm:
    def __init__(self, main):
        self.MainForm = main
        self.MainForm.window.title("Ресторан (администратор)")      #Изменение названия окна
        self.MainForm.create_console('Переход на панель администратора')        #Изменение текста в окне формы
        self.show_main_screen()                         #вызов собстевенного метода

    def show_main_screen(self):
        self.MainForm.active_elements['dish_help_label'] = create_label(font_color="#000000",
                                                                          text=f"Количество блюд в ресторане сейчас: {str(len(self.MainForm.dishes))}",
                                                                          position=[350, 0], background="#996600",
                                                                          font="Sedan 14")      #Создание рамки с текстом
        self.MainForm.active_elements['chose_what_do'] = create_label(font_color="#000000",
                                                                      text=f"Выберите действие:",
                                                                      position=[250, 600], background="#996600",
                                                                      font="Sedan 14")      #Создание рамки с текстом
        self.MainForm.active_elements['add_dish'] = create_button(font_color='#ffffff',
                                                                    text="Добавить Блюдо",
                                                                    command=self.add_dish,
                                                                    position=[480, 600], background='#996633',
                                                                    width='25', height='3', font="Sedan 12")        #Создание кнопки, при нажатии которой вызывает метод add_dish
        self.MainForm.active_elements['find_cost'] = create_label(font_color="#000000",
                                                                           text=f"Поиск по цене",
                                                                           position=[1000, 400], background="#996600",
                                                                           font="Sedan 14")     #Создание рамки с текстом
        self.MainForm.active_elements['find_cost_combo'] = create_combo_box(width=12, font_color="#000000",
                                                                               position=[1000, 450],
                                                                               values=VALUE, default=None,
                                                                               callback=self.show_find_cost, font="Sedan 14")       #Создание поля с выбором, которая вызывает метод show_find_cost
        self.MainForm.active_elements['show_dishes'] = create_button(font_color='#ffffff',
                                                                      text="Показать блюда",
                                                                      command=self.show_all_dishes,
                                                                      position=[740, 600], background='#996633',
                                                                      width='25', height='3', font="Sedan 12")          #Создание кнопки, при нажатии которой вызывает метод show_all_dishes
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff',
                                                                 text="Вернуться на основной экран",
                                                                 command=self.MainForm.return_to_main_screen,
                                                                 position=[1150, 800], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")           #Создание кнопки, при нажатии которой возвращает в главную форму
    def show_find_cost(self, event):                #метод поиска по цене
        exp_radius = self.MainForm.active_elements.get('find_cost_combo').get()         #получаем значение с поля с выбором
        text = f"Блюд с ценой {exp_radius}:"                    #передаем значение переменной text, где exp_radius это диапазон поиска
        count = 1                               #приравниваем количество к 1
        if exp_radius[0] == "0":                #если первое значение в диапазоне 0, то...
            start_exp = 0                       #начальное значение 0
        else:                                   #иначе
            start_exp = int(exp_radius[:3])     #начальное значение сравнения это первые 3 элемента строки, которые конвертируем в int
        stop_exp = int(exp_radius[-3] + exp_radius[-2] + exp_radius[-1])    #конечное значение диапазона это сумма последних 3 элементов строки, которые в последствии конверитруются в int
        for dish in self.MainForm.dishes:       #для dish в диапазоне, пока есть блюда
            if dish.cost in [i for i in range(start_exp, stop_exp+1)]:  #если цена в выбранном диапазоне, то...
                text += f'\n{count}) {dish.get_full_name()}'            #обновляем переменную text, в которую записываем количество попаданий и название блюда с ценой и типом блюда
                count += 1                                              #обновляем счетчик количества блюд с определнной ценой
        if text == f"Блюд с ценой {exp_radius}:":                       #если текст не изменился, то...
            text += "\nПо вашему запросу ничего не найдено"             #обновляем переменную text
        self.MainForm.create_console(text)                              #вызываем окно(консоль) в которую выводим text

    def return_to_admin_screen(self):                                   #метод возвращения на главный экран админа
        self.MainForm.create_console('Возврат в панель администратора') #вызываем окно(консоль) в которую выводим этот текст
        self.MainForm.destroy_all()                                     #Уничтожаем все элементы
        self.show_main_screen()                                         #показать главное меню, show_main_screen

    def add_dish(self):
        self.MainForm.destroy_all()                                     #Уничтожаем все элементы
        self.MainForm.create_console('Переход на страницу добавления блюда')    #вызываем окно(консоль) в которую выводим этот текст
        self.MainForm.active_elements['dish_label'] = create_label(font_color="#000000",
                                                                     text="Страница добавления блюда",
                                                                     position=[400, 40], background="#996600",
                                                                     font="Sedan 14")       #создание панели с текстом
        self.MainForm.active_elements['dish_name'] = create_label(font_color="#000000",
                                                                       text="Название блюда", position=[140, 150],
                                                                       background="#996600",
                                                                       font="Sedan 14")     #Создание панели с текстом
        self.MainForm.active_elements['dish_name_entry'] = create_entry(width=25, font="Sedan 14",
                                                                             position=[140, 200], font_color="#000000")     #Создание поля для ввода названия блюда
        self.MainForm.active_elements['dish_type_of_food'] = create_label(font_color="#000000",
                                                                    text="Тип блюда", position=[140, 250],
                                                                    background="#996600",
                                                                    font="Sedan 14")        #Создание панели с текстом
        self.MainForm.active_elements['dish_type_of_food_entry'] = create_combo_box(width=25, font_color="#000000",
                                                                              position=[140, 300],
                                                                              values=TYPE_OF_FOOD,
                                                                              font="Sedan 14", default=None)        #Создание поля с выбором для выбора типа блюда
        self.MainForm.active_elements['dish_quantity'] = create_label(font_color="#000000",
                                                                              text="Количество блюд",
                                                                              position=[140, 350], background="#996600",
                                                                              font="Sedan 14")      #Создание панели с текстом
        self.MainForm.active_elements['dish_quantity_entry'] = create_entry(width=25, font="Sedan 14",
                                                                                    position=[140, 400],
                                                                                    font_color="#000000")       #Создание поля для ввода количества блюд
        self.MainForm.active_elements['dish_weight'] = create_label(font_color="#000000",
                                                                    text="Вес блюда", position=[140, 450],
                                                                    background="#996600",
                                                                    font="Sedan 14")            #Создание панели с текстом
        self.MainForm.active_elements['dish_weight_entry'] = create_entry(width=25, font="Sedan 14",
                                                                          position=[140, 500],
                                                                          font_color="#000000")         #Создание поля для ввода веса блюда
        self.MainForm.active_elements['dish_cost'] = create_label(font_color="#000000",
                                                                          text="Цена Блюда", position=[140, 550],
                                                                          background="#996600",
                                                                          font="Sedan 14")          #Создание панели с текстом
        self.MainForm.active_elements['dish_cost_entry'] = create_entry(width=25, font="Sedan 14",
                                                                                position=[140, 600],
                                                                                font_color="#000000")       #Создание поля для ввода цены блюда
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")           #Создание кнопки, которая вызывает метод return_to_admin_screen
        self.MainForm.active_elements['complete'] = create_button(font_color='#ffffff', text="Выполнить",
                                                                  command=self.add_new_dish, position=[190, 650],
                                                                  background='#996633', width=20, height='3',
                                                                  font="Sedan 12")                        #Создание кнопки, которая вызывает метод add_new_dish

    def add_new_dish(self):
        type_of_food = self.MainForm.active_elements['dish_type_of_food_entry'].get()               #Получаем значение с нужного нам элемента
        name, name_flag = name_checker(self.MainForm.active_elements['dish_name_entry'].get())      #Получаем значение с нужного нам элемента
        cost, cost_flag = cost_checker(self.MainForm.active_elements['dish_cost_entry'].get())         #Получаем значение с нужного нам элемента
        quantity, quantity_flag = quantity_checker(self.MainForm.active_elements['dish_quantity_entry'].get())      #Получаем значение с нужного нам элемента
        weight, weight_flag = weight_checker(self.MainForm.active_elements['dish_weight_entry'].get())      #Получаем значение с нужного нам элемента
        if not name_flag:               #если имя введено неверно, то выводит ошибку
            self.MainForm.create_console(
                f"Название блюда введено неверно\n Учтите что длина названия не может превышать {MAXLENNAME} символов\nи не должна содержать цифры")
        if not cost_flag:               #если цена введена неверно, то выводит ошибку
            self.MainForm.create_console(
                f"Цена введена неверно\n Учтите что цена не может превышать {MAXCOST} ₽ \nили быть меньше 0 ₽")
        if not quantity_flag:               #если количество введено неверно, то выводит ошибку
            self.MainForm.create_console(
                f"Количество введено неверно\n Учтите что количество не может превышать {MAXQUANTITY} \nили быть меньше 0")
        if not weight_flag:               #если вес введен неверно, то выводит ошибку
            self.MainForm.create_console(
                f"Вес введен неверно\n Учтите что вес не может превышать {MAXWEIGHT} \nили быть меньше 0")
        exsist_flag = True              #флаг выхода
        if name_flag and quantity_flag and cost_flag and weight_flag:   #Если все флаги TRUE, то
            for dish in self.MainForm.dishes:               #для dish пока есть блюда
                print(dish.type_of_food, type_of_food)
                if dish.type_of_food == type_of_food.lower().title() and dish.name == name.lower().title() and dish.quantity == quantity and dish.cost == cost and dish.weight == weight:   #сравниваем значение введенного блюда со всеми имющимися блюдами, если есть повторения, то
                    exsist_flag = False     #флаг выхода ставим False и прерываем цикл
                    break
        if not exsist_flag:             #если флаг выхода False, то такое блюдо уже есть
            self.MainForm.create_console(
                f"Такое блюдо уже существует")
        if name_flag and quantity_flag and cost_flag and exsist_flag:   #Если все флаги блюда и флаг выхода, то добавляем в конец данные значения блюда, то есть добавляем блюдо в реестр и возрващаемся на главный экран админа
            self.MainForm.dishes.append(
                Dish(type_of_food=type_of_food, name=name, cost=cost, quantity=quantity, weight = weight))
            self.return_to_admin_screen()

    def show_all_dishes(self):              #метод вывода всех блюд
        self.MainForm.destroy_all()         #удаляем все элементы
        self.MainForm.active_elements['go_back'] = create_button(font_color='#ffffff', text="Назад",
                                                                 command=self.return_to_admin_screen,
                                                                 position=[1000, 700], background='#996633', width='25',
                                                                 height='3', font="Sedan 12")       #создаем кнопку, которая возвращает на главный экран админа

        text = ""       #объявление переменной
        count = 1       #объявление переменной
        for dish in self.MainForm.dishes:       #для dish пока есть блюда
            text = ''.join([text, f'\n{count}) ', dish.show_info()])    #добавление в текст кол-во блюд и всей информации о блюде
            count += 1                #обновление переменной
        if text == "":  #если текст не изменился, то блюд нет
            text += "Блюд пока нет"
        self.MainForm.create_big_console(text)   #вызываем окно(консоль) в которую выводим text
