import pickle

voc = {
    'стол': 'table',
    'стул': 'chair',
    'окно': 'window'
}


def print_voc():
    """
    Распечатывает ↑ словарь
    """
    print('Ныне словарь содержит:')
    for k, v in voc.items():
        print(k, '—', v)  # alt+0151


try:
    with open('files/dict.dat', 'rb') as dump_in:
        voc = pickle.load(dump_in)
except FileNotFoundError:
    with open('dict.dat', 'wb') as dump_out:
        pickle.dump(voc, dump_out)
    print('Создан словарь по умолчанию:')
    print_voc()

while True:
    temp = input('\nВведи слово для перевода или "#" для завершения: ')
    word = temp.strip().lower()
    if word == '#' or word == '№':
        break
    if word in voc:
        translation = voc[word]
        print(f'слово "{word}" переводится как {translation}')
    else:
        print(f'слово "{word}" отсутствует в словаре')
        translate = input(f'введите перевод для "{word}" или пустой ввод для пропуска: ')
        if translate:
            voc[word] = translate
            print(f'слово "{word}" с переводом {translate} внесено в словарь')
        else:
            print(f'перевод для "{word}" не добавлен')

with open('files/dict.dat', 'wb') as dump_out:
    pickle.dump(voc, dump_out)
