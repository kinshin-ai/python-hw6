#Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором

import random

#наполнение списка
list = []
for i in range(30):
    list.append(random.randint(1, 100))
print(f'исходный список: \n{list}')

#некорректно работает при внесении алгоритма сотртировки в функцию
'''def sorting(lst):
  for i in range(len(lst)):
        mins = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[mins]:
                mins = j
        lst[i], lst[mins] = lst[mins], lst[i]

print(f'сортированный список: \n{sorting(list)}')'''

#при сортировке циклом все работает
sort_list = list
for i in range(len(sort_list)):
  mins = i
  for j in range(i + 1, len(sort_list)):
    if sort_list[j] < sort_list[mins]:
      mins = j
  sort_list[i], sort_list[mins] = sort_list[mins], sort_list[i]

print(f'сортированный список: \n{sort_list}')
