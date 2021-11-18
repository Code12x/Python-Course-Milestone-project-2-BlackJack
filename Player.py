class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def get_hand_value(self):
        # Update self.hand_value
        self.hand_value = 0

        for card in self.hand:
            self.hand_value += card.get_value()

        # Adjust self.hand_value for aces
        aces = 0

        for card in self.hand:
            if card.get_rank() == "Ace":
                aces += 1

        while self.hand_value > 21 and aces:
            self.hand_value -= 10
            aces -= 1

        return self.hand_value

    def add_card(self, card):
        self.hand.append(card)

    def __str__(self):
        return self.name
