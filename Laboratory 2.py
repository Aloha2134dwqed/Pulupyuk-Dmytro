import itertools #Імпортується стандартний модуль Python для роботи з ітераторами (наприклад, генерація послідовностей, перестановки тощо).
from itertools import count #Імпортується функція count, яка створює нескінченну арифметичну прогресію.

'''
завдання дано список з елементами різних типів
'''










bebra ="Hello World" #рядки (тип str).
name ="Dmytro"       #рядки (тип str).
surname ="Pulupyuk"  #рядки (тип str).
age =16              #ціле число (тип int).

print(bebra)
print(name)
print(surname) #Вивід в консоль
print(age)

print(type(name))      #Функція type() використовується для визначення типу змінної.
print(type(surname))   #Виводиться тип змінних name, surname, age у консоль.
print(type(age))


count_int = 0          #Лічильники для кожного типу даних. Вони використовуватимуться для підрахунку кількості елементів кожного типу у списку.
count_str = 0
count_float = 0
count_set = 0
count_tuple = 0
count_bool = 0
count_list = 0
count_notnull = []    #Порожній список для фільтрування ненульових лічильників
max_value = 0         #Змінна для зберігання максимального значення серед лічильників.
lst_notnull = []      #Список для зберігання ненульових лічильників.
                   # список  /  логічні значення: True, False). /множини/числа з плаваючою комою, наприклад, 3.14/кортежі/рядки/цілі числа
lst_count_types = [count_list, count_bool, count_set, count_float, count_tuple, count_str, count_int]
lst = [name, surname, age]  #Список з елементами різних типів (name, surname, age).
lst_name_type = [int, str, str, int, str, str]  #Список типів, який використовується для ідентифікації домінуючого типу.
for item in lst:                        #Цей рядок означає, що ми перебираємо кожен елемент зі списку lst і зберігаємо його у змінній item.
    if type(item) == int:               #Якщо тип елемента (item) дорівнює int (ціле число), то збільшується останній лічильник у lst_count_types.
        lst_count_types[-1] +=1         #lst_count_types[-1] означає доступ до останнього елемента списку lst_count_types, який відповідає лічильнику для int.
    elif type(item) == str:             
        lst_count_types[-2] +=1
    elif type(item) == tuple:
        lst_count_types[-3] +=1
    elif type(item) == float:
        lst_count_types[-4] +=1
    elif type(item) == set:
        lst_count_types[-5] +=1
    elif type(item) == bool:
        lst_count_types[-6] +=1
    elif type(item) == list:
        lst_count_types[-7] +=1
for item in lst_count_types:
    if item !=0:
        lst_notnull.append(item)
    if len(lst_notnull) == 1:
        print('Good')
    else:
        if item > max_value:
            max_value = item

max_value = max(lst_count_types)        #Знаходження максимального значення
inn = lst_count_types.index(max_value)  #повертає індекс першого входження найбільшого значення в списку
print(lst_name_type[inn])               #inn — це індекс елемента в списку lst_name_type, який відповідає домінуючому типу даних.
for item in lst:                        #Перевіряється кожен елемент у списку lst.
    if type(item) !=lst_name_type[inn]: #Якщо тип елемента не збігається з домінуючим, виконується наступна дія:
        lst.remove(item)                #Видаляється елемент, який не відповідає домінуючому типу.