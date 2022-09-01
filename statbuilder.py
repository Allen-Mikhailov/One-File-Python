statstring = """
1	3000	170	52	20	36	0 	0 	0 
2	3107	186	59	23	41	0 	0 	0 
3	3224	204	67	27	47	0 	0 	0 
4	3353	223	76	31	53	0 	0 	0 
5	3495	244	86	36	60	5 	10 	0 
6	3651	267	97	41	68	5 	10 	0 
7	3823	293	109	47	76	5 	10 	0 
8	4012	321	122	53	85	5 	10 	0 
9	4221	352	136	60	95	10 	20 	0 
10	4451	387	152	68	106	10 	20 	0 
11	4704	425	170	76	118	10 	20 	0 
12	4983	467	189	85	131	10 	20 	0 
13	5290	513	210	95	146	10 	20 	0 
14	5628	564	233	106	162	10 	20 	0 
15	6000	620	259	118	180	10 	20 	0 
"""

collumnames = ["Level", "HP", "Attack", "Def", "Sp. Attack", "Sp. Def", "Crit Rate", "CDR", "Lifesteal"]
multi = [1, 5, 5, 5, 5, 5, 1, 1, 1]

collums = []

statstring = statstring.replace("\n", "")
statstring = statstring.replace("\t", " ")

for i in range(len(collumnames)):
    collums.append([])

i = 0
x = 0
while True:
    if statstring[i] != " ":
        s = statstring[i:statstring.index(" ", i)]
        num = int(s)

        collums[x].append(num * multi[x])

        i += len(s)
        x = (x+1)%9
    else:
        i += 1
        if i == len(statstring):
            break

datastring = "= {"
for i in range(15):
    datastring += "\n"
    datastring += "{"
    for x in range(len(collumnames)):
        datastring += "    [\""+collumnames[x] + "\"] = "+str(collums[x][i])+","
    datastring += "},"

datastring += "}"

f = open("statoutput.txt", "w")
f.write(datastring)
f.close()