# Основы Python 2
# TODO - отличие списков от кортежей
# TODO - задачки
# TODO - условный оператор if
# TODO - операторы цикла while, for
# TODO - однострочники

# Основы Python 3
# TODO - функции и параметры
# TODO - модули и параметры
# TODO - примеры применения внешних модулей

# Oтличие списков от кортежей

# # Это список list
# shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# # Это кортеж - неизменяемый список
# rainbow = ('Red', 'Green', 'Blue')

# # Проблема изменяемых объектов
# new_lst = shop_list
# new_lst.append('что-нибудь')
# print(new_lst)
# print(shop_list)
# print(id(shop_list) == id(new_lst))

# new_tpl = rainbow
# new_tpl = new_tpl + ('violet', )
# print(rainbow)
# print(new_tpl)
# print(id(rainbow) == id(new_tpl))

# кортеж работает быстрее чем список
# x, y = 1, 2

# Условный оператор if

# x = 4

# if x > 0:
#     print('x больше 0')
# elif x < 0:
#     print('x меньше 0')
# else:
#     print('х = 0')


# print('условие отработало')

# Циклы for while

# for - перебирает элементы внутри массива

# my_favorite_songs = [
#     ['Waste a Moment', 3],
#     ['New Salvation', 4],
#     ['Staying\' Alive', 3],
#     ['Out of Touch', 3],
#     ['A Sorta Fairytale', 5],
#     ['Easy', 4],
#     ['Beautiful Day', 4],
#     ['Nowhere to Run', 2],
#     ['In This World', 4],
# ]
    
# total = 0
# for i in my_favorite_songs:
#     #print(i[1])
#     total += i[1]

# print(total)


# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

# for price in room_prices:
#     if price == max(room_prices):
#         continue
   
#     if price == min(room_prices):
#         print('Минимальная цена:', price)
#         break 

#     print('Текущая цена:', price)
# else:
#     print('Такой цены нет!')

# print('До свидания!')


# for song, time in my_favorite_songs:
#     print(f'Название песни {song} - {time} минут')

# # цикл while
# i = 0
# while i < 10:
#     i = i + 1
#     print('i =', i)

# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

# i = -1
# while i < len(room_prices):
#     i += 1
#     price = room_prices[i] 
#     print('Проверяем ', price)
#     if price == min(room_prices):
#         print('Найдена минимальная цена')
#         break

#Однострочники

# Словари

# lst = [1, 2]
# tpl = (1, 2)
# dct = {''}

#нужно найти всех сотрудников, зарабатывающих 100 000 долларов и более
# employees = {'Alice' : 100000,
#             'Bob' : 99817,
#             'Carol' : 122908,
#             'Frank' : 88123,
#             'Eve' : 93121}

# Вариант 1
# top_mgrs = []
# for i in employees:
#     if employees[i] >= 100000:
#         top_mgrs.append(i)
# print(top_mgrs)

# Вариант 2

# top_mgrs = [i for i in employees if employees[i]>=100000]
# print(top_mgrs)

# ФУНКЦИИ И ПАРАМЕТРЫ

# Функция - блок кода, который можно вызывать с разными параметрами
# DRY - Dont Repeat Yourself

# Пример функции
# Внутри функции мы передаем параметры
# Создание функции

# def greeting(n):
#     print('Hello', n)

# # Вызов функции
# names = ['Марк', 'Мария','Семен']

# for i in names:
#     greeting(i)

#1
# employees = {'Alice' : 100000,
#             'Bob' : 99817,
#             'Carol' : 122908,
#             'Frank' : 88123,
#             'Eve' : 93121}

# def get_top_mgrs(empl: dict) -> list:
#     '''get_top_mgrs принимает словарь сотрудников и возвращает список сотрудников,
#     у которых з/п больше 100000.'''
#     top_mgrs = []
#     for i in empl:
#         if empl[i] >= 100000:
#             top_mgrs.append(i)
#     return top_mgrs
    
# salary = [employees[i]*2 for i in get_top_mgrs(employees)]
# print(salary)

# print(get_top_mgrs(employees))

# #2
# employees = {'Alice' : 100000,
#             'Bob' : 99817,
#             'Carol' : 122908,
#             'Frank' : 88123,
#             'Eve' : 93121}

# def get_top_mgrs(empl: dict) -> list:
#     '''get_top_mgrs принимает словарь сотрудников и возвращает список сотрудников,
#     у которых з/п больше 100000.'''
    
#     return [i for i in empl if empl[i]>=100000]
# salary = [employees[i]*2 for i in get_top_mgrs(employees)]
# print(salary)


a, b = 179, 37

def divine(a: int, b: int) -> int:
    '''divine целочисленно делит а на b'''
    counter = -1
    temp = a
    while temp >= 0:
        temp -= b
        counter += 1
    return counter
print(divine(200, 2))


# def trapezoid_s(a, b, h):
#     '''Функци􏰁 дл􏰁 рас􏰃ета пло􏰄ади трапеции. a - нижнее основание, b - верхнее основание, h - в􏰀сота.'''
#     return h * (a+b) / 2
# S = trapezoid_s(8, 4, 10) 
# print(S)

# МОДУЛИ И ИМПОРТ

# Варианты импорта
# import main
# main.foo()