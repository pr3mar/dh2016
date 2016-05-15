import pickle
#import urllib
import urllib.parse
import urllib.request
import json

redo_work = False

if redo_work:

    cs = [x[:-1] for x in open('../tweets.txt', 'r', encoding="utf8").readlines()] + \
         [x[:-1] for x in open('../dragonhack.txt', 'r', encoding="utf8").readlines()]

    #cs = [x.replace("HackKean", " ") for x in cs]
    #cs = [x.replace("https", "MajorLeagueHacking ") for x in cs]
    #cs = [x.replace("AnvilHackII", "UniversityOfLjubljana DragonHackLJ") for x in cs]
    #cs = [x.replace("AnvilHack", "DragonHack") for x in cs]
    #cs = [x.replace("CUCCHack", "DragonHack Ljubljana") for x in cs]

    mails = cs
    results = []
    for query in mails:
        try:
            data = urllib.parse.urlencode({"text": query}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)
            results.append((query, json.loads(u.read().decode("utf-8"))))
            print(results[-1])
        except:
            pass

    # print(results[0]["probability"]["neg"])
    # print(results[0]["label"])

    with open('results.pickle', 'wb') as handle:
      pickle.dump(results, handle)

else:
    with open('results.pickle', 'rb') as handle:
        results = pickle.load(handle)
    print("TOP 3 MOST POSITIVE TWEETS :)")
    for x in sorted([(x[0], x[1]['probability']['pos']) for x in results], key=lambda x: -x[1])[:3]:
        print(x)
    print(" ")
    print("TOP 3 MOST NEGATIVE TWEETS :(")
    for x in sorted([(x[0], x[1]['probability']['neg']) for x in results], key=lambda x: -x[1])[:3]:
        print(x)