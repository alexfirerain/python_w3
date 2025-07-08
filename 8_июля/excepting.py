print('Остаток от деления')

# try:
#     value = int(input('На что делим десять: '))
#     res = 10 % value
#     print(f'Остаток от деления 10 на {value} = {res}')
# except ZeroDivisionError:
#     print('на ноль не делим')
# except ValueError:
#     print('вводятся только числа')
# except Exception as exp:
#     print('Случилось исключение:', exp)
#     print('Случилось исключение:', type(exp))
#     print('Случилось исключение:', exp.__class__.__name__)

while True:
    try:
        value = int(input('На что делим десять: '))
        res = 10 % value
        print(f'Остаток от деления 10 на {value} = {res}')
        break  # лучше избегать в сложных алгоритмах
    except ZeroDivisionError:
        print('на ноль не делим')
    except ValueError:
        print('вводятся только числа')
    except Exception as exp:
        print('Случилось исключение:', exp)
        print('Случилось исключение:', type(exp))
        print('Случилось исключение:', exp.__class__.__name__)

to_exit = False
while not to_exit:
    try:
        value = int(input('На что делим десять: '))
        res = 10 % value
        print(f'Остаток от деления 10 на {value} = {res}')
    except ZeroDivisionError:
        print('на ноль не делим')
    except ValueError:
        print('вводятся только целые числа')
    except Exception as exp:
        print('Случилось исключение:', exp)
        print('Случилось исключение:', type(exp))
        print('Случилось исключение:', exp.__class__.__name__)
    else:
        to_exit = True

# бросаемся исключениями, хотя в Питоне оно "поднимается"
max_val = 10
min_val = 1

try:
    val = int(input(f'введите целое число от {max_val} до {min_val}: '))
    # инпут не понимает вариант принта только через запятую, ибо один аргумент у него
    if not min_val < val < max_val:
        raise ValueError('введено число не в допустимом диапазоне')
    print('число в корректном диапазоне')
except ValueError as exp:
    print('надо быть внимательнее:', exp)

# также юзаем УТВЕРЖДЕНИЯ:
try:
    text = input('введите текст: ')
    assert len(text) > 3  # это есть наше утверждение
except AssertionError:
    print('слишком краткий текст')  # в продакшене не принято, но в тестах

