'''
перевод из 10-й системы счисления в любую до 9
'''
# Ввод числа и преобразование к целому
num = int(input(':'))
# Ввод системы счисления
base = int(input("Base (2-9): "))

# Проверка корректности ввода системы счисления.
# Если основание не принадлежит указанному диапазону,
# то происходит выход из программы
if not(2 <= base <= 9):
    quit()

# Переменная для хранения строкового представления
# числа в заданной системе счисления
newNum = ''

# Пока исходное число больше 0,
while num > 0:
    # находится остаток от его деления на основание,
    # остаток преобразовывается к строковому типу и
    # добавляется в начало строкового представления нового числа
    newNum = str(num % base) + newNum
    # Само десятичное число делится нацело
    # на основание заданной системы счисления
    num //= base

# Вывод строкового представления числа
# в системе счисления с основанием base
print(newNum)
