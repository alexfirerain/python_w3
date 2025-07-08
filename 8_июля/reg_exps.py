# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# поиск по паттерну
import re
from random import sample

# банальный пример, эквивалентный find()
pattern = '20'
real_pattern = r'\b\w{4}\b'  # все слова из четырёх символов
test_string = '10 плюс 20 будет 31'
result = re.search(pattern, test_string)
print(result, type(result))
result = re.search(real_pattern, test_string)
print(result, type(result))
print(re.findall(real_pattern, test_string))
# Эр-строка это "raw-string"
next = 'дома было холодно'
print(re.findall(real_pattern, next))
"""

"""
dig_pat = r'\d'  # все цифры от 0 до 9
digs = re.findall(dig_pat, test_string)
print(digs)

# ТЕРНАРНЫЙ ОПЕРАТОР
print('цифры есть' if digs else 'цифр нет') # только присвоить нельзя
print('цифры есть' if re.findall(dig_pat, next) else 'цифр нет')

pat_3d = r'\d{3}' # три цифры вподряд
pat_ending = r'начало!\Z' # на что заканчивается
end_text = "Главное - начало!"
print(re.search(pat_ending, end_text))

pat = r'[0-5][0-9]' # две вподряд
print(re.findall(pat, "Время 07:45"))
pat_a = r'[а-я]'    # все маленькие буквы
pat_A = r'[а-яА-Я]' # все буквы
print(re.findall(pat_a, "Время 07:45"))
print(re.findall(pat_A, "Время 07:45"))

# исключение из поиска:
pat_exc = '[^ерм]'  # всё кроме е, р, м     # если нет ключей '\', 'r' не обязательно
print(re.findall(pat_exc, "Время 07:45"))

string = "Поиск по образцу (pattern)"
pat_extract = r'\((.+?)\)' # вытащить текст из скобок # ДЗ
print(re.findall(pat_extract, string))

# квантификаторы
# {m} - m раз
# {m,} - m раз и более
# {,m} - не более m раз
# {m,n} - от m до n раз (без пробела)
# ? - ноль или один (={0,1})
# * - от нуля и больше (={0,}) - точнее до 32767
# + - от одного и больше (={1,}) - точнее до 32767

pat_r = 'o{2,5}'
sample = "Gogle, Google, Gooogle, Gooooogle, Gooooooooogle"
print(re.findall(pat_r, sample))

pat_n = 'Go{2,}gle'
print(re.findall(pat_n, sample))

# ДЗ - регулярка, убирающая знаки препинания
