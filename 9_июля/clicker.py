class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        print(self._counter)

    def reset(self):
        self._counter = 0

device = Clicker()

for _ in range(37):
    device.click()

device.get_counter()

class Separator:
    def __init__(self):
        self._odds = []
        self._evens = []

    def add_num(self, num):
        self._odds.append(num) \
            if num % 2 != 0 \
            else self._evens.append(num)

    def get_odds(self):
        return self._odds

    def get_evens(self):
        return self._evens

