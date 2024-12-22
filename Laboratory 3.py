lst = [3,5,6,3,7,4,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("Лист до форматування ", lst)       #Ця команда виводить список lst на екран, щоб показати його початковий стан.
temp_str_list = []      #Це пусті списки, які будуть використовуватися для зберігання рядків (str) і чисел (int) із початкового списку.
temp_int_list = []
def remove_duplicates(a):     #Мета: Видалити всі дублікати зі списку a
    temp_list = []      #новий список для зберігання унікальних елементів.
    for i in a:         #Цикл for i in a: проходить через кожен елемент i у списку a.
        if i not in temp_list:     #перевіряє, чи немає цього елемента в temp_list.-!
            temp_list.append(i)                                              #Якщо немає, додаємо його:
    return temp_list         #Після проходження всього списку повертаємо


def counting(lst_for_counting):                         #-Мета: Поділити список на два — один із числами, інший із рядками.
    for item in lst_for_counting:
        if type(item) == str:           #перевіряє, чи є елемент рядком. Якщо так, додаємо його до temp_str_list
            temp_str_list.append(item)
        elif type(item) == int:       #перевіряє, чи є елемент числом. Якщо так, додаємо його до temp_int_list.
            temp_int_list.append(item)
    return temp_int_list, temp_str_list  #функція повертає два списки: числовий і текстовий.


def sortsis(lst_str_for_sort, lst_int_for_sort):
    sorted = [item.lower() if type(item) == str else item for item in lst_str_for_sort]
    sorted.sort()         #сортує рядки за алфавітом.
    lst_int_for_sort.sort()  #сортує числа за зростанням.
    return lst_int_for_sort + sorted   #об'єднує два списки: спочатку числа, потім рядки.


temp_lst = remove_duplicates(a=lst)    #видаляє дублікати з початкового списку lst та зберігає результат у temp_lst.
temp_int_list, temp_str_list = counting(temp_lst)   #розділяє temp_lst на два списки: temp_int_list для чисел.temp_str_list для рядків.
sortt = sortsis(temp_str_list, temp_int_list)       #сортує обидва списки та об'єднує їх.
print(sortt)          #Ця команда виводить фінальний відсортований список.