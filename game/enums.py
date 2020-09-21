from enum import Enum

class Suits(Enum):
    S = 40
    C = 60
    D = 80
    H = 100
    NO_SUIT = 0

class Cards(Enum):
    NINE = 0
    TEN = 10
    JACK = 2
    QUEEN = 3
    KING = 4
    ACE = 11

    def order_bias(self):
        val = 0

        if self is Cards.ACE:
            val = 20
        elif self is Cards.TEN:
            val = 16
        elif self is Cards.KING:
            val = 12
        elif self is Cards.QUEEN:
            val = 8
        elif self is Cards.JACK:
            val = 4

        return val