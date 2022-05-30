from random import shuffle

suite = 'Hearts Diamonds Spades Clubs'.split()
ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()

def __init__(self, suite, ranks):
    self.suite = suite
    self.ranks = ranks

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
