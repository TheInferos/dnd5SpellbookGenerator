import requests
import sqlite3


def get_columns():
    req = requests.get("http://dnd5eapi.co/api/spells/1").json()
    message = ""
    for key in req:
        message += str(key) + " text,"
    return message


def database_setup():
    database = sqlite3.connect("Data.db")
    c = database.cursor()
    c.execute('''CREATE TABLE spells(id INTEGER PRIMARY KEY,
                 name text,
                 school text,
                 level INTEGER, 
                 components text, 
                 material text,
                 casting_time text,
                 ritual text,
                 concentration text,
                 range text,
                 classes text,
                 subclasses text,
                 duration text,
                 page text,
                 desc text,
                 higher_level text
                 )''')
    database.commit()
    return database


def pass_spells(database):
    spell_list = []
    for spell_identifier in range(1, 306):   # at time of testing highest number
        req = requests.get("http://dnd5eapi.co/api/spells/" + str(spell_identifier)).json()
        spell_id = int(req["index"])
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
        s_range = str(req["range"])
        classes = ""
        for class_identifier in req["classes"]:
            classes += str(class_identifier["name"]) + " "
        duration = str(req["duration"])
        subclasses = ""
        for subclass_identifier in req["subclasses"]:
            subclasses += subclass_identifier["name"] + " "
        page = str(req["page"])
        desc = ""
        for desc_identifier in req["desc"]:
            desc += desc_identifier + "\n"
        if "higher_level" in req:
            higher_level = ""
            for higher_lvl_identifier in req["higher_level"]:
                higher_level += higher_lvl_identifier + "\n"
        else:
            higher_level = "n/a"
        spell = (
            spell_id,
            name,
            school,
            level,
            components,
            material,
            casting_time,
            ritual,
            concentration,
            s_range,
            classes,
            subclasses,
            duration,
            page,
            desc,
            higher_level
            )
        spell_list.append(spell)
    database.executemany(
        'INSERT INTO spells('
        'id,'
        'name,'
        'school,'
        'level,'
        'components,'
        'material,'
        'casting_time,'
        'ritual,'
        'concentration,'
        'range,'
        'classes,'
        'subclasses,'
        'duration,'
        'page,'
        'desc,'
        'higher_level'
        ') '
        'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        spell_list)
    database.commit()



