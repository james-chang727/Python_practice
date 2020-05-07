"""A Coin object represents a coin with 2 sides that can be flipped."""

import random

class Coin:
    # Constants
    HEADS = 0
    TAILS = 1

    # Static variables
    heads_so_far = 0
    tails_so_far = 0

    # Constructor initializes the state of new Coin objects.
    def __init__(self):
        # set the attributes (the state in each Coin object)
        self.flip()

    def flip(self):
        self._face = random.randint(0, 1)
        if self._face == Coin.HEADS:
            Coin.heads_so_far += 1
        else:
            Coin.tails_so_far += 1

    def get_heads_so_far(self):
        return Coin.heads_so_far

    def get_tails_so_far(self):
        return Coin.tails_so_far

    def __str__(self):
        if self._face == Coin.HEADS:
            the_face = "H"
        if self._face == Coin.TAILS:
            the_face = "T"
        return the_face
