import os, json

emails = {}
count = 0
for dir in os.listdir("emails_by_address"):

    if dir.find("enron.com") < 0:
        count += 1
        continue

    if dir[:5] == "from_":
        user_first = dir[5:-4]
        mode = "from"
    else:
        user_first = dir[3:-4]
        mode = "to"

    if not (user_first in emails):
        emails[user_first] = {"to": {}, "from": {}}

    with open("emails_by_address/" + dir) as file:
        for line in file:
            start = line.find("maildir/")
            end = line.find("/", start + 8)
            user_second = line[start + 8:end]
            if not (user_second in emails[user_first][mode]):
                emails[user_first][mode][user_second] = 1
            else:
                emails[user_first][mode][user_second] += 1

corrected_users = {}
for user_first in emails:
    for user_second in emails[user_first]["to"]:
        try:
            splitted = user_second.split("-")
            splitted = [x[0] for x in sorted([(x, len(x)) for x in splitted], key=lambda x: x[1], reverse=True)]
        except Exception as e:
            continue
        for check in emails:
            check = check[:check.find("@")].replace(".", "")
            idx = check.find(splitted[0])
            if idx > 0:
                check = check[:idx]
            elif idx == 0:
                check = check[len(splitted[0]):]
            else:
                continue
            try:
                if check[0] == splitted[1]:
                    corrected_users["-".join(splitted)] = emails[user_first]
                else:
                    continue
            except Exception:
                corrected_users[splitted[0]] = emails[user_first]

print(json.dumps(corrected_users, indent=1))
# print(len(emails))
# print(count)
