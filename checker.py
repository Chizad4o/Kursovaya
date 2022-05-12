from constants import ADMINPASSWORD, MAXCOST, MAXLENNAME, MAXQUANTITY, MAXWEIGHT, MAXEXPERIENCE, MAXTABLE


def check_correct_admin_password(pas):
    if pas == ADMINPASSWORD:
        return True
    return False


def no_digit(text):
    for i in text:
        if i.isdigit():
            return False
    return True


def name_checker(text):
    if len(text) > 1 and len(text) < MAXLENNAME:
        flag1 = True
    else:
        flag1 = False
    flag2 = no_digit(text)
    return text, flag1 and flag2

def table_checker(text:str):
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXTABLE:
        return text, False
    return int(text), True

def quantity_checker(text:str):
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXQUANTITY:
        return text, False
    return int(text), True

def weight_checker(text:str):
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXWEIGHT:
        return text, False
    return int(text), True

def cost_checker(text:str):
    for i in text:
        if not i.isdigit():
            return text, False
    if int(text) < 0 or int(text) > MAXCOST:
        return text, False
    return int(text), True
