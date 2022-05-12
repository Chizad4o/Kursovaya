CONSOLETEXT = 'Результат Ваших действий: '

DOCTOR_PROFESSIONS = ["Терапевт", "Окулист", "Ухо горло нос"]
DIAGNISIS = {
    DOCTOR_PROFESSIONS[0]: ['Диагноз 1', 'Диагноз 2'],
    DOCTOR_PROFESSIONS[1]: ['Диагноз 3', 'Диагноз 4'],
    DOCTOR_PROFESSIONS[2]: ['Диагноз 5', 'Диагноз 6'],
}

TYPE_OF_FOOD = ["Салат", "Суп", "Горячее", "Напитки"]

DIAGNISISLIST = []
for dig in DIAGNISIS.values():
    DIAGNISISLIST.extend(dig)


ADMINPASSWORD = '1'
MAXLENNAME = 20
MAXCOST = 900
MAXQUANTITY = 200
MAXWEIGHT = 1500
MAXEXPERIENCE = 100
MAXTABLE = 20
MAXTABLEVALUE = [f'{i}' for i in range(1, MAXTABLE+1, 1)]
VALUE = [f'{i-100}-{i}' for i in range(100, MAXCOST+100, 100)]