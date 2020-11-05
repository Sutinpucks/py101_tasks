"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass
import re
pw = input('Enter your password: ')
if len(pw) >= 8 and re.search(r'[A-Za-z]', pw) and  re.search(r'[0-9]', pw):
    print('strong')
else:
    print('weak')