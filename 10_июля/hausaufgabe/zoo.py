from animals import Cat, Dog, Elephant
import random, time

class Zoo:
    def __init__(self):
        self._animals = [Cat(), Dog(), Elephant()]

    def make_all_sounds(self):
        print("Доносятся звуки:")
        while True:
            if random.random() > 0.1:
                random.choice(self._animals).make_sound()
                time.sleep(random.random() * 1.5)
            else:
                print("…и тишина…")
                break

def main():
    print("Добро пожаловать в наш зверопарк «Дом Дядюшки Питона»!\n"
          "Вводите любые символы, чтобы ходить по нему и прислушиваться.\n"
          "Для выхода введите 0")
    zoo = Zoo()
    while input("Погуляем по зверопарку? ") != "0":
        zoo.make_all_sounds()
    print("До свидания! Заходите к нам ещё, когда будет больше зверей и функционала!")

main()