import Charecter


class Wizard:
    def __init__(self, level, int_mod):
        self.level = level
        self.Slots = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        self.memorisedSpells = self.update_memorised_spells(int_mod)

    def level_up(self):
        self.level += 1
        self.update_slots()

    def update_slots(self):
        slots = {1: [[2], [0], [0], [0], [0], [0], [0], [0], [0]],
                 2: [[3], [0], [0], [0], [0], [0], [0], [0], [0]],
                 3: [[4], [2], [0], [0], [0], [0], [0], [0], [0]],
                 4: [[4], [3], [0], [0], [0], [0], [0], [0], [0]],
                 5: [[4], [3], [2], [0], [0], [0], [0], [0], [0]],
                 6: [[4], [3], [3], [0], [0], [0], [0], [0], [0]],
                 7: [[4], [3], [3], [1], [0], [0], [0], [0], [0]],
                 8: [[4], [3], [3], [2], [0], [0], [0], [0], [0]],
                 9: [[4], [3], [3], [3], [1], [0], [0], [0], [0]],
                 10: [[4], [3], [3], [3], [2], [0], [0], [0], [0]],
                 11: [[4], [3], [3], [3], [2], [1], [0], [0], [0]],
                 12: [[4], [3], [3], [3], [2], [1], [0], [0], [0]],
                 13: [[4], [3], [3], [3], [2], [1], [1], [0], [0]],
                 14: [[4], [3], [3], [3], [2], [1], [1], [0], [0]],
                 15: [[4], [3], [3], [3], [2], [1], [1], [1], [0]],
                 16: [[4], [3], [3], [3], [2], [1], [1], [1], [0]],
                 17: [[4], [3], [3], [3], [2], [1], [1], [1], [1]],
                 18: [[4], [3], [3], [3], [3], [1], [1], [1], [1]],
                 19: [[4], [3], [3], [3], [3], [2], [1], [1], [1]],
                 20: [[4], [3], [3], [3], [3], [2], [2], [1], [1]]}
        self.Slots = slots[self.level]

    def update_memorised_spells(self, int_mod):
        return self.level + int_mod


char = Wizard(4, 4)
print char.memorisedSpells