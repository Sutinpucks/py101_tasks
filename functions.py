"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def is_even(*numbers):
    for num in numbers:
        if num % 2 == 0:
            print('There is at least one even number in input')
            return True
    print('There are no even numbers in input')
    return False
    
is_even(12, 5, 54, 4) # test 
is_even(1, 1111, 5)  # test

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
sell_alcohol() if age > 21 else print ('Мы не продаём алкоголь несовершеннолетним.')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_keyword(check_str):
    import keyword
    return keyword.iskeyword(check_str)

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."


def get_type(object):
    types_translate = {'int': 'число', 'str': 'строка', 'bool': 'булевый', 'NoneType': 'None',
     'tuple': 'кортеж', 'set': 'множество', 'dictionary': 'словарь'}
    return "Это " + types_translate[type(object).__name__]



print(get_type('s')) # test
print(get_type('44')) # test 
print(get_type(44)) # test