from constants import ADMINPASSWORD, MAXCOST, MAXLENNAME, MAXQUANTITY, MAXWEIGHT, MAXTABLE


def check_correct_admin_password(pas):  #метод для проверки корректности ввода пароля
    if pas == ADMINPASSWORD:            #если введен вверно, то возвращаем True
        return True
    return False                        #иначе False


def no_digit(text):                     #метод для проверки на наличие цифр, если есть цифры возврщаем False
    for i in text:
        if i.isdigit():
            return False
    return True


def name_checker(text):                 #метод для проверки названия блюда, по длине, и на наличие цифр
    if len(text) > 1 and len(text) < MAXLENNAME:
        flag1 = True
    else:
        flag1 = False
    flag2 = no_digit(text)
    return text, flag1 and flag2


def table_checker(text:str):            #метод для проверки правильности введения номера столика
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXTABLE:
        return text, False
    return int(text), True

def quantity_checker(text:str):         #метод для проверки правильности введения кол-во блюд
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXQUANTITY:
        return text, False
    return int(text), True

def quantity_checker_for_order(text:str):            #метод для проверки правильности введения кол-во блюд для заказа
    if text == '':
        text = '0'
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXQUANTITY:
        return text, False
    return int(text), True

def weight_checker(text:str):            #метод для проверки правильности введения веса блюда
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXWEIGHT:
        return text, False
    return int(text), True

def cost_checker(text:str):            #метод для проверки правильности введения цены блюда
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXCOST:
        return text, False
    return int(text), True
