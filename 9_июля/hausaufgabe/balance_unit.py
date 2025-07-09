class Balance:
    def __init__(self):
        self._right = 0
        self._left = 0

    if __name__ == '__main__':
        print('для проверки работы весов запустите файл balance_demo.py')

    def add_left(self, weight: int) -> None:
        """
        Добавляет вес в левую чашу
        :param weight: вес, кладомый в левую чашу
        :raises ValueError: если вес отрицательный
        """
        if weight < 0:
            raise ValueError('Снятие веса не поддерживается в текущей версии')
        self._left += weight

    def add_right(self, weight: int) -> None:
        """
        Добавляет вес в левую чашу
        :param weight: вес, кладомый в правую чашу
        :raises ValueError: если вес отрицательный
        """
        if weight < 0:
            raise ValueError('Снятие веса не поддерживается в текущей версии')
        self._right += weight

    def result(self) -> str:
        """
        Возвращает результат взвешивания, согласно заданию
        :return: текстовое сообщение о том, какая чаша перевесила
        """
        return 'весы в равновесии' if self._is_balanced() \
            else 'левая чаша перевесила' if self._left > self._right \
            else 'правая чаша перевесила'

    def reset(self) -> str:
        """
        Опустошает обе чаши весов
        :return: сообщение о том, что весы обнулены
        """
        self._left = 0
        self._right = 0
        return 'весы сброшены'

    def get_status(self) -> str:
        """
        Сообщает текущее состояние весов
        :return: текстовое сообщение о весе на обеих чашах
        """
        return f'на левой чаше {self._left}, на правой чаше {self._right}'

    def get_difference(self) -> int:
        """
        Возвращает разницу веса между чашами весов
        :return: положительное число, если левая чаша тяжелее,
                отрицательное число, если правая чаша тяжелее,
                0, если весы в равновесии
        """
        return self._left - self._right

    def get_difference_percentage(self) -> float:
        """
        Возвращает в процентах от веса более лёгкой чаши,
        на сколько вторая чаша тяжелее.
        :return: положительное число, если левая чаша тяжелее,
                отрицательное число, если правая чаша тяжелее,
                0, если весы в равновесии
        """
        if self._is_balanced():
            return 0.0
        havier_scale = max(self._left, self._right)
        lighter_scale = min(self._left, self._right)
        if lighter_scale == 0:
            return float('inf') if self._left > self._right else -float('inf')
        ratio = ((havier_scale / lighter_scale) - 1) * 100
        return ratio if self._left > self._right else -ratio

    def _is_balanced(self) -> bool:
        """
        Проверяет, находятся ли весы в равновесии
        :return: ИСТИНУ, если весы в равновесии, ЛОЖЬ в противном случае
        """
        return self._left == self._right
