class Car:
    counter = 0
    def __init__(self, brand, model, color):
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

    # экземплярные объекты создаются в ините и принадлежат объекту
    # если они определены просто в классе (и без сэлф) — классные, статические поля
    # https://indo-european.eu/2019/01/assh-reread-i-y-dna-haplogroups-among-indo-europeans-apart-from-r1b-l23/

