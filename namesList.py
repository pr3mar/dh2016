import json

with open('data.json') as file:
    namesData = json.load(file)

names = set()
for n in namesData:
    names.add(n)

with open('names.txt', 'w') as text_file:
    for name in names:
        text_file.write(name+"\n")