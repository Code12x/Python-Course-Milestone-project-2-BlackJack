class Card:

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
        self.value = self.calculate_value(self.rank)

    def calculate_value(self, rank):
        values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                  "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
        return values[rank]

    def get_rank(self):
        return self.rank

    def get_suite(self):
        return self.suite

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return self.rank + " of " + self.suite