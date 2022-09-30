# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. Количество предикатов генерируется случайным образом от 5 до 11, проверяем это утверждение 10 раз,
# с помощью модуля time выводим на экран , сколько времени отработала программа.

# 10 раз проверили это утверждения, количество предикатов случайное от 5 до 11 через randint,
# само значение предикатов тож случайное через choice как вариант

from random import *
ar = [True, False]
num = randint(5, 11)
array = [choice(ar) for _ in range(num)]
print(array)


# def boolean_algebra(x, y, z):
#     print(f'¬({x} V {y} V {z}) = \
# ¬{x} ⋀ ¬{y} ⋀ ¬{z} is \
# {(not (x or y or z)) == (not x and not y and not z)}')
#     return (not (x or y or z)) == (not x and not y and not z)

# if (boolean_algebra(0, 0, 0)
#     or boolean_algebra(0, 0, 1)
#     or boolean_algebra(0, 1, 1)
#     or boolean_algebra(1, 1, 1)
#     or boolean_algebra(1, 0, 0)
#     or boolean_algebra(1, 1, 0)
#     or boolean_algebra(0, 1, 0)
#     or boolean_algebra(1, 0, 1)):
#     print("True")
# else:
#     print("False")

from random import *
ar = [0, 1]
num = range(1, 4)
array = list(choice(ar) for _ in num)
print(array)


И еще один способ создать список - это генераторы списков. 
Генератор списков - способ построить новый список, применяя выражение к каждому элементу последовательности. Генераторы списков очень похожи на цикл for.

>>>
>>> c = [c * 3 for c in 'list']
>>> c
['lll', 'iii', 'sss', 'ttt']