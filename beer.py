def sevenfive(i):
    print "%s Bottles of Miller Lite, take one down, pass it around, %s bottles of Miller lite!" % (i, i - 1)
    return True
def seven(i):
    print "%s Bottles of Lite, take one down, pass it around, %s bottles of lite!" % (i, i - 1)
    return True
def five(i):
    print "%s Bottles of Miller, take one down, pass it around, %s bottles of Miller" % (i, i - 1)
    return True
def beer():
    for i in range(100, 1, -1):
        print i
        (i % 7 == 0 and i % 5 == 0 and sevenfive(i)) or (i % 7 == 0 and seven(i)) or (i % 5 == 0 and five(i))

beer()