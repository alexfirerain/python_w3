# пишем свой модуль

def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


print(__name__)

if __name__ == '__main__':
    print('это библиотека, а исполняется main')
else:
    print('это и есть исполнение')
