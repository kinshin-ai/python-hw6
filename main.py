#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_size = int(input('введите размер списка: '))
list = []
for i in range(list_size):
  list.append(int(input('введите число: ')))
print (list)


def summarize (lst):
  total = 0
  for x in range (len(lst)):
    if x%2 != 0:
      total =  total + lst[x]
  return total

print(summarize(list))