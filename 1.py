#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов. Определить количество элементов, кратных 3 и индексы
#последнего такого элемента.

# Ввод списка из 10 элементов
# Ввод списка из 10 элементов
list_a = []
for i in range(10):
    element = int(input(f"Введи элимент {i + 1}: "))
    list_a.append(element)

# Определение количества элементов, кратных 3
count_multiples_of_three = 0
indices_of_multiples_of_three = []

for index, element in enumerate(list_a):
    if element % 3 == 0:
        count_multiples_of_three += 1
        indices_of_multiples_of_three.append(index)

# Вывод результатов
print(f"A: {list_a}")
print(f"числа кратны 3: {count_multiples_of_three}")

if count_multiples_of_three > 0:
    print(f"Индексы кратны 3: {indices_of_multiples_of_three}")
else:
    print("В списке нет элементов кратных 3")
