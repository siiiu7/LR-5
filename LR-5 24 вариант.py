'''
Лабораторная работа №5
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
Вариант 24.
F(1) = 3; F(2) = 3; F(w) = 5*F(w-1)-4*F(w-2) при w > 2.
'''
import sys
import time
import matplotlib.pyplot as plt
import pylab

# -------------------------Ввод-------------------------

n = input('Введите натуральное число: ')

try:
    n = int(n)
except ValueError:
    sys.exit('Введено не натуральное число, или не число вовсе. Программа завершена.')

if n < 1:
    sys.exit('Введено не натуральное число. Программа завершена.')


# -----------------------Рекурсия------------------------

def recursive_f(number):
    if number == 1 or number == 2:
        return 3
    return 5 * recursive_f(number - 1) - 4 * recursive_f(number - 2)


# ------------------------Итерация------------------------

def iterative_f(number):
    if number == 1 or number == 2:
        return 3

    f_prev = 3
    f_curr = 3

    for i in range(3, number + 1):
        f_next = 5 * f_curr - 4 * f_prev
        f_prev, f_curr = f_curr, f_next

    return f_curr


# ---------------------------------------------------------
recursion_time = []
iteration_time = []
num_list = []

# вычисление функции и замер времени для каждого числа от 1 до n
for i in range(1, n + 1):
    num_list.append(i)

    # рекурсия
    start_time = time.time()
    recursive_result = recursive_f(i)
    recursion_time.append(time.time() - start_time)

    # итерация
    start_time = time.time()
    iterative_result = iterative_f(i)
    iteration_time.append(time.time() - start_time)

    # проверка результатов
    assert recursive_result == iterative_result, f'Ошибка в вычислении. Результаты различны для числа {i}.'

# вывод результатов в табличной форме
print(f'| {"Число":<5} | {"Рекурсия":<15} | {"Итерация":<15} |')
print('-' * 40)
for i in range(n):
    print(f'| {num_list[i]:<5} | {recursion_time[i]:<15.10f} | {iteration_time[i]:<15.10f} |')

# вывод результатов в графической форме
plt.plot(num_list, recursion_time, label='Рекурсия')
plt.plot(num_list, iteration_time, label='Итерация')
plt.title('Производительность функции F')
plt.xlabel('Входное число')
plt.ylabel('Время вычисления, с')
plt.legend()
plt.show()