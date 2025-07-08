# подключаем свой модуль
import my_lib

# from . lib import summ # т.е. из текущей директории
# from .. lib import summ # т.е. из родительской директории
# from .lib import summ # т.е. импорт относительно текущего файла

# запускаемый файл в программе один, остальные подгружаемые модули
# когда файл запускается, он для себя называется "__main__"
# сначала сделать по ТЗ (чтобы не было пиздежу, делай всё по чертежу)

from my_lib import diff # etc
from my_lib import summ

# from package_1.module_july import greet
from package_1 import greet, average     # "относительный экспорт", если импорты определены в '/package_1/__ini__.py'

#
# from package_1 import _hidden_function # не работает



print(my_lib.diff(7, 12))

# интересный приём разобраться, кто исполняет, а кто библиотека
# __name__ обращается к имени чего-либо
a = 3
print(type(a).__name__)
print(__name__)  # при подгрузке модулей, они исполняются целиком (в начале имя импортнутого выведено)


def main():
    print(summ(7, 3))


if __name__ == '__main__':
    main()

if __name__!= '__main__':
    print('это библиотека')

# ещё у нас есть файл init - он обозначает себя пакетом
# модули с одним именем могут быть в разных пакетах

print(greet('The World'))

import package_1
# print(package_1.module._hidden_function())  # так можно, но не следует делать

print(average(100, 1000))

print('Автор', package_1.__author__)

# Д/з см. методичка "Модули"