import json
import re

regex = re.compile('http\S+')

with open('FacebookHashtags/dragonhack.json') as data_file:
    dataDragonhack = json.load(data_file)

with open('FacebookHashtags/hackathon.json') as data_file:
    dataHackathon = json.load(data_file)

with open('FacebookHashtags/majorleaguehacking.json') as data_file:
    dataMajorLeagueHacking = json.load(data_file)

with open('FacebookHashtags/mlhacks.json') as data_file:
    dataMlhacks = json.load(data_file)

with open("dragonhack.txt", "w") as text_file:
    for d in dataDragonhack["result"]:
        wr = re.sub(regex, "", d["content"])
        text_file.write(wr.encode('ascii', 'ignore').decode('ascii')+"\n")

    for d in dataHackathon["result"]:
        wr = re.sub(regex, "", d["content"])
        text_file.write(wr.encode('ascii', 'ignore').decode('ascii') + "\n")

    for d in dataMajorLeagueHacking["result"]:
        wr = re.sub(regex, "", d["content"])
        text_file.write(wr.encode('ascii', 'ignore').decode('ascii') + "\n")

    for d in dataMlhacks["result"]:
        wr = re.sub(regex, "", d["content"])
        text_file.write(wr.encode('ascii', 'ignore').decode('ascii') + "\n")
