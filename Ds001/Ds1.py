# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    list = ['Понедельник' , 'Вторник' , 'Среда' , 'Четверг' , 'Пятница' , 'Суббота' , 'Воскресенье']
    weekday = int(input('Введите день недели: '))
    weekday = weekday - 1
except:
    print('!! Введите целое число !!')

if weekday > 6 or weekday < 0:
    print('Такого дня нет')
elif weekday == 5 or weekday == 6:
    print(f'{list[weekday]} - является ли этот день выходным? -> ДА')
else:
    print(f'{list[weekday]} - является ли этот день выходным? -> НЕТ')