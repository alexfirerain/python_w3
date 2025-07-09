class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self):
        self.words.append(input("ввод слова: "))

    def result(self):
        return sorted(self.words, key=lambda x: len(x))

