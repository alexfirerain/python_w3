import pymorphy3
from pymorphy3 import MorphAnalyzer

# Линтеры контролируют следование кода лучшим практикам,
# к нему ещё два плагина:
#    flake8-bugbear находит распространённые логические ошибки в коде
#    pep8-naming проверяет имена на соответствие PEP8

morph = pymorphy3.MorphAnalyzer()
print(morph.parse('пила'))

form = MorphAnalyzer().parse('бутылка')[0]

for btl in reversed(range(99)):
    print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl + 1)[0]} ряженки')
    print('Выпьем бутылочку')
    if btl % 10 == 1 and btl != 11:
        remain = "Осталась"
    else:
        remain = "Осталось"
    print(f'{remain} {btl} {form.make_agree_with_number(btl + 1)[0]} ряженки')

# собеседование зависит от людей и их настроения