import Spell


class SpellBook:
    def __init__(self):
        self.spell_list = [[], [], [], [], [], [], [], [], [], []]



    def add_spell(self, add_spell):
        self.spell_list[add_spell.get_level()].append(add_spell)

    def get_spell_names(self):
        spell_names = [[], [], [], [], [], [], [], [], [], []]
        for level in range(len(self.spell_list)):
            for spell in range(len(self.spell_list[level])):
                spell_names[level].append(self.spell_list[level][spell].name)
        return spell_names





def test():
    spell_book = SpellBook()
    spell_book.create_spell_book_level_min_max(20)
    test_spell = Spell.Spell({"level": 4})
    spell_book.add_spell(test_spell)
    #print spell_book.spell_list
