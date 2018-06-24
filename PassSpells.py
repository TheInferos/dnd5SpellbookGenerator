import requests
import sqlite3


def getCollumns():
    req = requests.get("http://dnd5eapi.co/api/spells/1").json()
    message = ""
    for key in req:
        message += str(key) + " text,"
    return message


def databaseSetup():
    db = sqlite3.connect("Data.db")
    c = db.cursor()
    c.execute('''DROP TABLE spells''')
    c.execute('''CREATE TABLE spells(id INTEGER PRIMARY KEY,
                 name text,
                 school text,
                 level INTEGER, components text, material text,
        casting_time text,ritual text,concentration text,range text,classes text,subclasses text,duration text,page text,desc text,higher_level text)''')
    db.commit()
    return db


def passSpells(db):
    spell2 = []
    for i in range(1, 306):
        req = requests.get("http://dnd5eapi.co/api/spells/" + str(i)).json()
        id = int(req["index"])
        name = str(req["name"])
        school = str(req["school"]["name"])
        level = int(req["level"])
        components = ""
        for char in req["components"]:
            components += char + " "
        components = str(components)

        if "M" in components:
            if "material" in req:
                material = req["material"]
            else:
                material = "unknown materials"
            # material = "mats Required"
        else:
            material = "n/a"
        casting_time = str(req["casting_time"])
        ritual = str(req["ritual"])
        concentration = str(req["concentration"])
        sRange = str(req["range"])
        classes = ""
        for i in req["classes"]:
            classes += str(i["name"]) + " "
        duration = str(req["duration"])
        subclasses = ""
        for i in req["subclasses"]:
            subclasses += i["name"] + " "
        page = str(req["page"])
        desc = ""
        for i in req["desc"]:
            desc += i + "\n"
        if "higher_level" in req:
            higher_level = ""
            for i in req["higher_level"]:
                higher_level += i + "\n"
        else:
            higher_level = "n/a"
        spell = (
        id, name, school, level, components, material, casting_time, ritual, concentration, sRange, classes, subclasses,
        duration, page, desc, higher_level); # TODO: Remove semicolon
        spell2.append(spell)
    db.executemany(
        'INSERT INTO spells(id,name,school,level,components,material,casting_time,ritual,concentration,range,classes,subclasses,duration,page,desc,higher_level) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (spell2))
    db.commit()
db = databaseSetup()
passSpells(db)

# db.executemany('''INSERT INTO spells(id,name,school,level,components,material,casting_time,ritual,concentration,Range,classes,subclasses,duration,page,desc,higher_level)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', tuple(spells))
