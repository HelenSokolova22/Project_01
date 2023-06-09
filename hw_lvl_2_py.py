
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

arr = [4,6,2,1,9,63,-134,566] 

def minimum(arr):
  n = len(arr)
  i = 0
  while i < n-1:
    j=0
    while j < n-1-i:
      if arr[j] > arr [j+1]:
        arr[j],arr[j+1] = arr[j+1], arr[j]
      j+=1
    i +=1
  return arr
min = minimum(arr)    
print('min =',min[0])

def maximum(arr):
  n = len(arr)
  i = 0
  while i < n-1:
    j=0
    while j < n-1-i:
      if arr[j] > arr [j+1]:
        arr[j],arr[j+1] = arr[j+1], arr[j]
      j+=1
    i +=1
  return arr
max = maximum(arr)    
print('max =',max[-1])

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


year = {'1':'(январь)','2':'(февраль)','3':'(март)','4':'(апрель)','5':'(май)','6':'(июнь)','7':'(июль)','8':'(август)','9':'(сентябрь)','10':'(октябрь)','11':'(ноябрь)','12':'(декабрь)'}
q = 'является частью первого квартала'
w = 'является частью второго квартала'
e = 'является частью третьего квартала'
r = 'является частью четвертого квартала'
month = int(input('месяц '))

def quarter_of(month:dict) -> str:
 
  if 1<=month<=12:
    if month == 1:
      print(year['1'], q)
    if month == 2:
      print(year['2'],q)
    if month == 3:
      print(year['3'],q)
    if month == 4:
      print(year['4'],w)
    if month == 5:
      print(year['5'],w)
    if month == 6:
      print(year['6'],w)
    if month == 7:
      print(year['7'],e)
    if month == 8:
      print(year['8'],e)
    if month == 9:
      print(year['9'],e)
    if month == 10:
      print(year['10'],r)
    if month == 11:
      print(year['11'],r)
    if month == 12:
      print(year['12'],r)
  else:
    return('Такого месяца нет!')

quarter_of(month)

# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

number = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

def switch_it_up(number):
  for i in number:
    number = str(number[i])
    return number.format(str(number))

switch_it_up(number)

# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

foo = "Hi! Hello!"

def remove_exclamation_marks(s):
  exclamation_marks = {ord('!') : None}
  return s.translate(exclamation_marks)


remove_exclamation_marks(foo)

from os import remove
# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


def remove_last_em(s):
