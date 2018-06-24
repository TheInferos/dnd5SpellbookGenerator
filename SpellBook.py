import spell


class SpellBook:
    def __init__(self):
        self.minS = []
        self.maxS = []
        self.spellList = [[], [], [], [], [], [], [], [], [], []]

    def create_spell_book_level_min_max(self, wiz_lvl):
        min_s = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        max_s = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, wiz_lvl):
            lvl = i // 2
            min_s[lvl] += 2
            for j in range(lvl + 1):
                max_s[j] += 2
        self.minS = min_s
        self.maxS = max_s[0:9]

    def spell_added(self, spell_level):
        pos = spell_level - 1
        for i in range(pos):
            self.maxS[i] -= 1
        self.minS[pos] -= 1

    def add_spell(self, add_spell):
        s_lvl = add_spell.get_level()
        self.spell_added(s_lvl)
        self.spellList[s_lvl].append(add_spell)


def test():
    spell_book = SpellBook()
    spell_book.create_spell_book_level_min_max(20)
    test_spell = spell.Spell({"level": 4})
    spell_book.add_spell(test_spell)
    print spell_book.spellList


test()
