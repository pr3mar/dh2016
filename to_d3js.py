import json, os

with open("data.json", "r") as data:
    data = json.load(data)
    toSave = []
    for entry in data:
        tmp = {"source": entry}
        for fst in data[entry]["from"]:
            tmp["target"] = fst
            tmp["type"] = "outgoing"
            tmp["noSent"] = data[entry]["from"][fst]
        toSave.append(tmp)
        tmp = {"target": entry}
        for snd in data[entry]["to"]:
            tmp["source"] = snd
            tmp["type"] = "ingoing"
            tmp["noSent"] = data[entry]["to"][snd]
        toSave.append(tmp)
    out = open(os.getcwd() + "/viz/libs/viz.js", "w")
    out.write("links = " + json.dumps(toSave, indent=1))
