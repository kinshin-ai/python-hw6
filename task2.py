#Написать программу, которая генерирует двумерный массив на A x B элементов (A и B вводим с клавиатуры), и считаем средне-арифметическое каждой строки

import random

#задание размеров массива
rows = int(input('количество строк: '))
cols = int(input('количество столбцов: '))
list = [[] for i in range(rows)]

#наполнение массива случайными числами
for i in range(rows):
    for j in range(cols):
        list[i].append(random.randint(1, 100))

#вывод сгенерированного массива
for i in range(0, len(list)):
    for i2 in range(0, len(list[i])):
        print(list[i][i2], end=' ')
    print()

#вычисление среднего арифметического в каждой строке
for i in range(rows):
    sum = 0
    for j in range(cols):
        sum = sum + list[i][j]
    print(f'Среднее арифметическое {i+1}-ой строки: {sum/cols}')