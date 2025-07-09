class Car:
    counter = 0
    def __init__(self, brand="Иж", model="Сатурн", color="красный"):
        self.engine_on = False
        Car.counter += 1    # к статичным обращаемся через имя класса
        self.brand = brand
        self.model = model
        self.color = color

        print('конструктор выполнен')   # конструктор выделяет объекту память и наделяет свойствами

    def start_engine(self):
        self.engine_on = True  # можно объявить свойство в методе за счёт ссылки на класс!
                               # но тогда он появляется только после запуска этого метода!

    def drive_to(self, target):
        if self.engine_on:
            print(f"едем в {target} на {self.brand} {self.model}")
        else:
            print("не едем")

    @staticmethod
    def get_count():
        return Car.counter

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def is_engine_on(self):
        return self.engine_on


# экземплярные объекты создаются в ините и принадлежат объекту
# если они определены просто в классе (и без сэлф) — классные, статические поля
# https://indo-european.eu/2019/01/assh-reread-i-y-dna-haplogroups-among-indo-europeans-apart-from-r1b-l23/
# сборщик мусора не лазит внутрь капсулы! там всё живёт столько же, сколько объект
