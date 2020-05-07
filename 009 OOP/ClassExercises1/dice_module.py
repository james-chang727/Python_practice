"""A Dice object represents a dice with 6 sides that can be casted"""

import random

class Dice:

    dice_ref = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

    # Constructor initializes the state of new Dice objects.
    def __init__(self):
        # set the attributes (the state in each Dice object)
        self.cast()

    def cast(self):
        self._face = random.randint(1, 6)

    def get_face(self):
        return self._face

    def __str__(self):
        return Dice.dice_ref.get(self.get_face())

