# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# a) решение
from itertools import takewhile,count
generator = [el for el in (takewhile(lambda el: el<11, count(3)))]
print(generator)

# b) первый вариант для б)

from itertools import cycle
def func(list):
    c=0
    for el in cycle(list):
        print (el, end=' ')
        c += 1
        if (c>30):
            break

list = [1, 3, 5, 10, 4, 7, 95, 12]
func(list)

# альтернативный вариант для б)
def func(list):
    c=0
    for el in cycle(list):
        if (c >len(list)-1 ):
            break
        c +=1
        yield el

list = [1, 3, 5, 10, 4, 7, 95, 12]
new_list=[i for i in func(list)]
print(new_list)

