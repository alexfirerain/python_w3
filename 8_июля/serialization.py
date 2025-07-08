"""
Сериализация и десериализация не безопасны, они часто используются,
дампуем объект в файл.
Десериализация неизвестных файлов вирусоопасна
"""
import pickle  # засолка (огурцов)
import pprint

dic = {
    'стол': 'table',
    'стул': 'chair'
}
# сериализация
with open('files/my_dic.sex', 'wb') as pick:
    pickle.dump(dic, pick)

# десериализация
with open('files/my_dic.sex', 'rb') as source:
    d = pickle.load(source)

pprint.pprint(d, width=15)
