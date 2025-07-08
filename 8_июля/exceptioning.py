# самое известное исключение NameError
# в компилируемых языках именованных исключений меньше
# это не ошибка, а ситуация прерывания логики

# fo = open('incognita')
# обёртка трайик-сэпт

try:
    fo = open('files\\phallus', encoding='UTF-8')
    print(fo.read())
except FileNotFoundError:
    with open('files\\phallus', 'w', encoding='UTF-8') as fo:
        fo.write('по умолчанию')
    print('файл не найден, создан фаллос по умолчанию')
#     это плохо тем, что на каждое исключение надо свой блок
else:
    print('файл открыт успешно, прочтём и закроем')
    print(fo.read())
    fo.close()
finally:
    print('продолжаем разговор')

"""
какова структура исключения:
try:
    что хотим выполнить
except:
    если тип исключения не указан, обрабатываются все, это не рекомендуется
    здесь обработка исключения
else:
    выполняется, если исключений не было
filnally:
    выполняется напоследок в любом разе
    
"""
# работать с файлами следует в обёртках исключениеобработчиков

flag = False  # открывался ли на запись

try:
    fo = open('files\\phallus', encoding='UTF-8')
except FileNotFoundError:
    fo = open('files\\phallus', encoding='UTF-8')
    flag = True
    print('файл не найден, создан фаллос по умолчанию')
else:
    print('открыт')
    print(fo.read())
    fo.close()
finally:
    if flag:
        fo.write('default')
        fo.close()
        print('continue')
# ?!
    if not fo.closed:
        fo.close()

#  хороший программист не ждёт исключений, создаёт их сам
