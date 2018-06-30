from Tkinter import *
import Wizard


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("DND Spells")


def main_menu():
    frame = GUI()
    generate_wizard_spellbook = Button(frame.window, text="Generate\nWizard\nSpellbook",
                                       command=generate_spellbook_method)
    generate_wizard_spellbook.pack()
    generate_wizard_spellbook.place(bordermode=OUTSIDE, height=100, width=100)
    frame.window.mainloop()


def generate_spellbook_method():
    frame = GUI()
    level_scale = Scale(frame.window, from_=1, to=20, orient=HORIZONTAL, label="Wizard Level")
    level_scale.pack()
    subclass = Listbox(frame.window)
    subclass_list = ["Bladesinging", "Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion",
                 "Necromancy", "Transmutation", "War Magic"]
    for i in range (len(subclass_list)):
        subclass.insert(i, subclass_list[i])
    subclass.select_set(0)
    subclass.pack()
    go = Button(frame.window, text="Generate That Wizard",
                command=lambda: Wizard.Wizard(level_scale.get(), 4, subclass_list[subclass.curselection()[0]]).wizard_from_gui())
    go.pack()

def test():
    main_menu()


test()
