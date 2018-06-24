import spell
class Spellbook():
    def __init__(self):
        self.minS = []
        self.maxS = []
        self.spellList=[[],[],[],[],[],[],[],[],[],[]]

    def createSpellbookLevelMinMax(self,wizLvl):
        minS = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        maxS = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        maxL = wizLvl // 2
        for i in range(1, wizLvl):
            lvl = (i) // 2
            minS[lvl] += 2
            for j in range(lvl + 1):
                maxS[j] += 2
        self.minS = minS
        self.maxS = maxS[0:9]
    def spellAdded(self,sLevel):
        pos = sLevel-1
        for i in range(pos):
            self.maxS[i] -= 1
        self.minS[pos] -= 1

    def addSpell(self,spell):
        sLvl = spell.getLevel()
        self.spellAdded(sLvl)
        self.spellList[sLvl].append(spell)

def Test():
    spellbook = Spellbook()
    spellbook.createSpellbookLevelMinMax(20)
    Spell = spell.Spell({"level": 4})
    spellbook.addSpell(Spell)
    print spellbook.spellList
Test()