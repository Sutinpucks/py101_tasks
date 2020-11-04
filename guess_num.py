"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass
import random
u_number = None
secret_num = random.randrange(0,1000000)
while u_number != secret_num:
    u_number = input('Enter your number ')
    if u_number == '' or u_number == 'exit':
        break
    elif u_number.isdigit() == False:
        print('Not a number')
    elif int(u_number) not in range(0,1000000):
        print('Your number is out of range')
    elif int(u_number) == secret_num:
        print('Bullseye! You`are right!')
        break
    else:
        print('Secret number is bigger' if int(u_number) < secret_num else 'Secret number is lower')
    