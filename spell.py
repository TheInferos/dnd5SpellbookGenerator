class Spell:
    def __init__(self, data):
        self.level = data["level"]

    def get_level(self):
        return self.level
