import random
from typing import overload


class Dictogram(dict):
    def __init__(self, iterable=None):
        # dict.__init__(self)
        super(Dictogram, self).__init__()
        self.n_unique = 0
        self.n_tokens = 0

        if iterable:
            self.update(iterable)

    def update(self, iterable, **F):
        for item in iterable:
            if item in self:
                self[item] += 1
                self.n_tokens += 1
            else:
                self[item] = 1
                self.n_tokens += 1
                self.n_unique += 1

    def get(self, item, k=0):
        return super(Dictogram, self).get(item, k)

    def return_random_word(self):
        rand_key = random.sample(self.keys(), 1)
        return rand_key[0]

    def return_weighted_random_word(self):
        rand_int = random.randint(0, self.n_tokens - 1)
        ind = 0
        keys_list = list(self.keys())
        for i in range(self.n_unique):
            print(self[keys_list[i]])
            ind += self[keys_list[i]]
            if ind > rand_int:
                return keys_list[i]


c = Dictogram(['a', 'b', 'b', 'b', 'c'])
print(c.return_weighted_random_word())
