import math


def getAround(x, y):
    if y%2 == 0:
        return [
            (x-1, y),
            (x-1, y+1),
            (x+1, y),
            (x-1, y-1),
            (x, y-1),
            (x, y+1),
        ]
    else:
        return [
            (x-1, y),
            (x+1, y+1),
            (x+1, y),
            (x+1, y-1),
            (x, y-1),
            (x, y+1),
        ]

tileDict = {}

class tile:
    def __init__(self, pos, energy):
        self.pos = pos
        self.energy = energy
        tileDict[str(pos)] = self

        if energy > 0:
            for npos in getAround(pos[0], pos[1]):
                if npos in tileDict:
                    tileDict[str(npos)].tap(self)
                else:
                    tile(npos, energy-1)

    def tap(self, tile):
        self.energy = max(tile.energy, self.energy)

def calculate(radius):
    tileDict.clear()
    tile((0, 0), radius)
    del tileDict[str((0, 0))]
    
    positions = []
    for _tile in tileDict:
        positions.append(tileDict[_tile].pos)

    # When y % 2 == 1
    tileDict.clear()
    tile((0, 0), radius)
    del tileDict[str((0, 0))]
    ypositions = []
    for _tile in tileDict:
        ypositions.append(tileDict[_tile].pos)

    return [positions, ypositions]

file = open("./hexagons.txt", "w")
file.write("{\n")
maxsize = 8
for i in range(1, maxsize+1):
    _string = str(calculate(i)).replace("(", "{").replace(")", "}").replace("[", "{").replace("]", "}")
    file.write(_string+",\n")

file.write("}")

file.close()