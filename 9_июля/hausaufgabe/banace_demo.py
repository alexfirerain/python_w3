from balance_unit import Balance

WELCOME = """
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *  Добро пожаловать в демонстрацию возможностей весов «Баланс-0.1»! *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    Вы можете добавлять вес в произвольных единицах на левую или правую чашу.
        Для этого введите команду вида "X вес", где X - это указатель чаши, а вес - это число.
        Для левой чаши используются указатели: Л, L, S
        Для правой чаши используются указатели: П, R, D
        Текущая версия программы поддерживает только целочисленный ввод.
        Контроль консистентности единиц ввода на вашей ответственности.
        Мы предполагаем, что все здесь взрослые люди.
    Команды для вывода результата:
        ? - выводит сообщение о текущем балансе весов
        ?+ - сообщает, на сколько больше веса в какой чаше
        ?* - сообщает, насколько больше веса в одной чаше в сравнении с другой
        ?? - выводит вес на обеих чашах
    Для сброса и обнуления обеих чаш весов наберите команду "000"
    Для завершения работы наберите команду "---"
"""
LEFT_TRIGGERS = 'ЛLSKЫДCС'
RIGHT_TRIGGERS = 'ПRDGКВЗPР'


def main():
    balance = Balance()

    print(WELCOME)
    while (command := input('> ').strip().upper()) != "---":
        if command == "000":
            print(balance.reset())

        elif command == "?":
            print(balance.result())

        elif command == "??":
            print(balance.get_status())

        elif command == "?+":
            difference = balance.get_difference()
            print('на чашах одинаково веса' if difference == 0 else \
                      f'левая чаша тяжелее на {difference}' if difference > 0 else \
                          f'правая чаша тяжелее на {-difference}')

        elif command == "?*":
            relative_difference = balance.get_difference_percentage()
            print('никакая чаша не тяжелее' if relative_difference == 0 else \
                      f'левая чаша тяжелее на {relative_difference:3.2f}% от правой' if relative_difference > 0 else \
                          f'правая чаша тяжелее на {-relative_difference:3.2f}% от левой')

        elif len(command) <= 1:
            print('неверная команда')

        else:
            try:
                key = command[0]
                value = int(command[1:].strip())
                if key in LEFT_TRIGGERS:
                    balance.add_left(value)
                elif key in RIGHT_TRIGGERS:
                    balance.add_right(value)
                else:
                    print('неверная команда')
            except ValueError as ex:
                print('ошибка ввода:', ex)

    print('Спасибо за интерес к взвешиванию!')

main()
