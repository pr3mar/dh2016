import json
import numpy as np

with open('data.json') as file:
    namesData = json.load(file)

names = []
with open('names.txt') as lista:
    for l in lista:
        names.append(l[:-1])

matrica = np.zeros((len(names), len(names)))

i = 0
for name in names:
    j = 0
    for name2 in names:
        if name2 in namesData[name]["to"]:
            matrica[i,j] = namesData[name]["to"][name2]
        j += 1
    i += 1

np.savetxt("matrica.csv", matrica, fmt='%i', delimiter=",")