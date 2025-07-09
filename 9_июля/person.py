class Person:
    def __init__(self, name='Homo', age=1):
        self._name = name  # к закрытым полям обращаться можно, но не следует
        self._age = age  # ибо Питон это для взрослых людей

    def person_info(self):
        print(f'чел с именем {self._name} и возрастом {self._age}')

    def set_name(self, new_name):  # это сеттер
        if new_name:
            self._name = new_name
        else:
            print("не допускаются пустые имена")

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print(new_age, "не допустимое значение возраста")

    # а вот и геттеры
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


p = Person()
print(p._age)
print(p._name)
p.person_info()
p.set_age(345)