import DataBase
import random
import SpellBook
import Spell


class Wizard:
    def __init__(self, level, int_mod, sub_class):
        self.level = level
        self.slots = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        self.memorised_spells = 0
        self.total_known_spells = 0
        self.max_memorised_spells = self.update_memorised_spells(int_mod)
        self.sub_class = sub_class
        self.spell_book = SpellBook.SpellBook()
        self.total_number_spells, self.max_spells_per_level = self.create_spell_book_level_min_max()

    def level_up(self):
        if self.level < 20:
            self.level += 1
            self.update_slots()

    def create_spell_book_level_min_max(self):
        max_spells = [6, 0, 0, 0, 0, 0, 0, 0, 0]
        total = 0
        for i in range(1, self.level):
            lvl = i // 2
            total += 2
            for j in range(lvl + 1):
                if j > 8:
                    pass
                else:
                    max_spells[j] += 2
        return total, max_spells

    def spell_added(self, spell_level):
        pos = spell_level
        for i in range(pos):
            self.max_spells_per_level[i] -= 1

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
        self.slots = slots[self.level]

    def update_memorised_spells(self, int_mod):
        return self.level + int_mod

    def get_highest_slot_left(self):
        max_level = 0
        for spell_level in range(len(self.max_spells_per_level)):
            if self.max_spells_per_level[spell_level] > 0:
                max_level = spell_level
        return max_level
    
    def add_memorised_spell(self, spell):
        self.spell_book.add_spell(spell)
        self.spell_added(spell.level)
        self.total_number_spells -= 1
        self.memorised_spells += 1
        self.total_known_spells += 1

    def add_ritual_spell(self, spell):
        self.spell_book.add_spell(spell)
        self.spell_added(spell.level)
        self.total_number_spells -= 1
        self.total_known_spells += 1

    def check_if_known(self, spell_checked):
        known_already = False
        for spell in self.spell_book.spell_list[spell_checked.level - 1]:
            if spell.name == spell_checked.name:
                known_already = True
        return known_already

    def generate_spell_book(self):
        data_base = DataBase.DataBase()
        needed_rituals = self.total_number_spells - self.max_memorised_spells
        highest_slot = (self.level+1) // 2
        if highest_slot >= 9:
            highest_slot = 9
        rand = random
        for i in range(highest_slot):
            rows = data_base.query_spell("classes LIKE ? and level =? ", ("%Wizard%", (i+1)))
            place = rand.randint(0, len(rows)-1)
            self.add_memorised_spell(Spell.Spell(rows[place]))
            memorised_slots_left = True
        max_level = self.get_highest_slot_left()
        rows = data_base.query_spell("level <=? AND classes LIKE ? AND level >0", (max_level +1, "%Wizard%"))
        while memorised_slots_left:
            random_spell_identifier = rand.randint(0, len(rows)-1)
            random_spell = Spell.Spell(rows[random_spell_identifier])
            if self.max_spells_per_level[random_spell.level-1] >= 1:
                self.add_memorised_spell(random_spell)
                if self.max_memorised_spells - self.memorised_spells <= 0:
                    memorised_slots_left = False
            rows.remove(rows[random_spell_identifier])
        if self.max_spells_per_level[0] == 0:
            slots_left = False
        else:
            slots_left = True
        max_level = self.get_highest_slot_left()
        rows = data_base.query_spell("ritual =? AND level <=? AND classes LIKE ? AND level >0",
                                     ("yes",max_level + 1, "%Wizard%"))
        while slots_left:
            random_spell_identifier = rand.randint(0, len(rows) - 1)
            random_spell = Spell.Spell(rows[random_spell_identifier])
            if self.max_spells_per_level[random_spell.level - 1] >= 1:
                known_already = self.check_if_known(random_spell)
                if known_already == False:
                    self.add_ritual_spell(random_spell)
                if self.slots[0] == 0 or len(rows) == 1:
                    slots_left = False
            rows.remove(rows[random_spell_identifier])
            if len(rows) == 0:
                slots_left = False
        if self.max_spells_per_level[0] >= 1:
            rows = data_base.query_spell("level <=? AND classes LIKE ? AND level >0",
                                         (max_level + 1, "%Wizard%"))

            while self.max_spells_per_level[0] > 0:
                random_spell_identifier = rand.randint(0, len(rows) - 1)
                random_spell = Spell.Spell(rows[random_spell_identifier])
                if self.max_spells_per_level[random_spell.level - 1] >= 1:
                    known_already = self.check_if_known(random_spell)
                    if not known_already:
                        self.add_memorised_spell(random_spell)
                rows.remove(rows[random_spell_identifier])

    def print_spells(self):
        spells = self.spell_book.get_spell_names()
        for level in range(len(spells)):
            print "level ", level
            for spell in spells[level]:
                print spell

    def wizard_from_gui(self):
        self.generate_spell_book()
        self.print_spells()



def test():
    char = Wizard(2, 4, "Evocation")
    char.generate_spell_book()
    char.print_spells()

