# дан список: введите индекс и получите значение
values = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]
while True:
    try:
        try:
            index = int(input('введи индекс: '))
        except ValueError:
            raise ValueError("ввод не распознаётся как индекс")
        if not -len(values) <= index < len(values):
            raise ValueError("индекс за пределами массива")
    except ValueError as ve:
        print("ошибка ввода:", ve)
    else:
        print(f'число по индексу {index} это {values[index]}')
        break

# переписать на исключения:
while True:
    a = input('введи первое число ')
    b = input('введи второе число ')

    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print('на ноль не делим')
        else:
            print(int(a) / int(b))
            break
    else:
        print('тока числа вводили бы')

while True:
    try:
        a = input('введи первое число ')
        b = input('введи второе число ')

        if not a.isdigit() or not b.isdigit():
            raise ValueError('тока числа приемлемы здесь!')

        a, b = int(a), int(b)

        if b == 0:
            raise ValueError('здесь не делят на ноль!')

        print(a / b)
        break
    except Exception as e:
        print('ошибка:', e)
