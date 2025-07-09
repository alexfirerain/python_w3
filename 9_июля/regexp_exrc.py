import re


# https://regex101.com
# интересные приёмы:
# ремув пунктуацию


def remove_punctuation(input_str: str) -> str:
    """
    Методом sub() заменяем все найденные совпадения пустой строкой
    и возвращаем очищенную.
    :param input_str: строка съ знаками препинания
    :return: строку без знаков препинания
    """
    return re.sub(r'[^\w\s]', '', input_str)


test_str = "Язык Питон, будучи *** интуитивно понятным)), прост для изучения!"
print(remove_punctuation(test_str))

fruit_str = '   яблоко,груша.   Банан; слива!абрикос'
split_pat = r'[,.;!:]'
print(re.split(split_pat, fruit_str))

# убрать и пробелы тоже №1
print([w.strip() for w in re.split(split_pat, fruit_str)])

# убрать и пробелы тоже №2
print(re.split(split_pat, ''.join(fruit_str.split())))

# убрать и пробелы тоже №3
print(list(map(lambda x: x.strip(), re.split(split_pat, fruit_str))))

print(sorted(x.strip() for x in re.split(split_pat, fruit_str)))