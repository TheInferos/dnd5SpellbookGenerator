class Spell:
    def __init__(self, data):
        self.spell_id = data[0]
        self.name = data[1]
        self.school = data[2]
        self.level = data[3]
        self.components = data[4]
        self.material = data[5]
        self.casting_time = data[6]
        self.ritual = data[7]
        self.concentration = data[8]
        self.s_range = data[9]
        self.classes = data[10]
        self.subclasses = data[11]
        self.duration = data[12]
        self.page = data[13]
        self.desc = data[14]
        self.higher_level = data[15]

    def get_level(self):
        return self.level
