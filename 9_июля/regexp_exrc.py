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
