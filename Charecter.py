
def getInt():
    gotNum = False
    while gotNum == False:
        Int = raw_input("(please use a valid integer\n")
        gotNum = checkInt(Int)
    return Int

def getMod(int):
    return (int//2)-5

def checkInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def getWizLvL():
    print "Please Specify the Wizzards level?"
    getInt()

def getIntelligence():
    print "Please specify the wizards Intelligence?"
    getInt()
