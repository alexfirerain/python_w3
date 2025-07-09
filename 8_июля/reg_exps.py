# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# поиск по паттерну
import re

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
# если символ есть метасимвол (из управляющих в регулярках), экранируется он
# скобки в регулярке — "группа захвата"
# в принципе r'' лучше указывать даже когда нет особых символов

pattern_g = r'стеклянн?ый'  # "стекляный" и "стеклянный" подходят (вторая 'н' от 0 до 1 раз)

glass_str = "стекляный, стеклянный, оловянный, серебряный"
print(re.findall(pattern_g, glass_str))


gr_pat = r'<img.*>' # вот какой жадина

# метод match() ищет что-то в начале строки
# метод search() ищет по всей строке до первого вхождения
# метод findall() ищет все вхождения
html_rag = 'Картинка <img src="bg.jpg"> в тексте</p>'
print(re.findall(gr_pat, html_rag))

lazy_pat = r'<img.*?>' # lazy / non-greedy
print(re.findall(lazy_pat, html_rag))

# жадный квантификатор (greedy quantifier)
greed_pat = r'<img[^>]+src="([^">]+)"'
print(re.findall(greed_pat, html_rag))

site_sample = '<b>Вот начало:</b><p>Содержание</p><i>примечания</i>'
# как вытащить содержимое?
ext_pat = '<p>(.*?)</p>' # лениво
print(re.findall(ext_pat, site_sample))

new_site_text = '<b></b><p align = "center"></p>'
# тэг с атрибутами сломал наш план
new_site_pat = r'<p[^>]*>(.*)</p>' # или более лениво r'<p[^>]*>(.*?)</p>'
print(re.findall(new_site_pat, site_sample))

