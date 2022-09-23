# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = input("Enter the operation sign: ")
    if y != 0:
        if z == '+':
            print(f'{x + y}')
        elif z == '-':
            print(f'{x - y}')
        elif z == '/':
            print(f'{x / y}')
        elif z == '*':
            print(f'{x * y}')
        elif z == 'mod':
            print(f'{x % y}')
        elif z == 'div':
            print(f'{x // y}')
        else:
            z == 'pow'
            print(f'{x ** y}')
    else:
        print("Division by 0!")

except:
    print("Enter an integer")
