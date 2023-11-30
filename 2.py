#!/usr/bin/python3
# -*- coding: utf-8 -*-

#19. В списке, состоящем из вещественных элементов, вычислить:
#1. произведение положительных элементов списка;
#2. сумму элементов списка, расположенных до минимального элемента.
#Упорядочить по возрастанию отдельно элементы, стоящие на четных местах, и элементы,
#стоящие на нечетных местах.



numbers = [float(x) for x in input("Введите числа через пробел: ").split()]

# 1. Произведение положительных чисел
positive_product = 1
for number in numbers:
    if number > 0:
        positive_product *= number

# 2. Сумма чисел до минимального
min_index = numbers.index(min(numbers))
sum_before_min = sum(numbers[:min_index])

# 3. Упорядочивание чисел на четных и нечетных местах
even_numbers = sorted(numbers[1::2])
odd_numbers = sorted(numbers[0::2])

# Вывод результатов
print(f"Исходные числа: {numbers}")
print(f"Произведение положительных чисел: {positive_product}")
print(f"Сумма чисел до минимального: {sum_before_min}")
print(f"Четные числа (упорядочены): {even_numbers}")
print(f"Нечетные числа (упорядочены): {odd_numbers}")