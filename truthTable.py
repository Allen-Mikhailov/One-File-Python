import math
import pandas as pd

equasion = input("Type in the equasion to calculate: ")

# Getting Variables
variables = {}
variableList = []
variableA = equasion.replace("&", "").replace("|", "").replace("(", "").replace(")", "").split(" ")
for i in range(len(variableA)):
    if variableA[i] != "":
        variableList.append(variableA[i])
        variables[variableA[i]] = True

class partClass:
    def __init__(self, p1, p2, operator):
        self.p1 = p1
        self.p2 = p2
        self.operator = operator

    def calc(self):
        p1 = False
        p2 = False

        if type(self.p1) == partClass:
            p1 = self.p1.calc()
        else:
            p1 = variables[self.p1]

        if type(self.p2) == partClass:
            p2 = self.p2.calc()
        else:
            p2 = variables[self.p2]

        match self.operator:
            case "&&":
                return p1 and p2
            case "||":
                return p1 or  p2

def toPart(rawParts):
    parts = []
    i = 0
    while i < len(rawParts):
        if rawParts[i] == "(":
            part = ""
            for j in range(i+1, rawParts.index(")")):
                part += rawParts[j]+" "
                i += 1
            i += 1
            parts.append(toPartStr(str))
        else:
            parts.append(rawParts[i])
        i += 1

    hasOpp = False

    # Finding &&
    for i in range(len(parts)):
        if parts[i] == "&&":
            newpart = partClass(parts[i-1], parts[i+1], "&&")
            parts.pop(i-1)
            parts.pop(i-1)
            parts.pop(i-1)
            parts.insert(i-1, newpart)

            hasOpp = True
            break

    # Finding ||
    for i in range(len(parts)):
        if parts[i] == "||":
            newpart = partClass(parts[i-1], parts[i+1], "||")
            parts.pop(i-1)
            parts.pop(i-1)
            parts.pop(i-1)
            parts.insert(i-1, newpart)

            hasOpp = True
            break

    if hasOpp:
        parts = toPart(parts)
        pass

    if (len(parts) == 1):
        return parts[0]


    return parts
        
def toPartStr(str):
    rawParts = str.split(" ")
    return toPart(rawParts)

data = []
for i in range(int(math.pow(2, len(variableList)))):
    row = []
    
    for j in range(len(variableList)):
        varValue = ((i >> j) & 0x1) == 0
        variables[variableList[j]] = varValue
        row.append(varValue)


    print(toPartStr(equasion))
    row.append(toPartStr(equasion)[0].calc())
    data.append(row)
    

columns = variableList.copy()
columns.append(equasion)


df = pd.DataFrame(data, columns=columns)
df.to_csv("./TruthTable.csv")