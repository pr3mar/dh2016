import os, json

emails = {}
for dir in os.listdir("emails_by_address"):
    if dir.find("enron.com") < 0:
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

out = open("raw_data.json", "w")
out.write(json.dumps(emails, indent=1))

corrected_users = {}
splitted = set()
for user_first in emails:
    for user_second in emails[user_first]["from"]:
        tmp = user_second.split("-")
        tmp = tuple(x[0] for x in sorted([(x, len(x)) for x in tmp], key=lambda x: x[1], reverse=True))
        splitted = splitted | set([tuple(tmp)])
print(len(splitted))

for tuple in splitted:
    print(tuple)
    for check in emails:
        tmp = check[:check.find("@")].replace(".", "")
        idx = tmp.find(tuple[0])
        if idx > 0:
            tmp = tmp[:idx]
        elif idx == 0:
            tmp = tmp[len(tuple[0]):]
        else:
            continue
        if not ("-".join(tuple) in corrected_users):
            corrected_users["-".join(tuple)] = emails[check]

out = open("corrected_data.json", "w")
out.write(json.dumps(corrected_users, indent=1))



# for check in emails:
#     tmp = check[:check.find("@")].replace(".", "")
#     idx = tmp.find(splitted[0])
#     if idx > 0:
#         tmp = tmp[:idx]
#     elif idx == 0:
#         tmp = tmp[len(splitted[0]):]
#     else:
#         continue
#     try:
#         if tmp[0] == splitted[1] and not "-".join(splitted) in corrected_users:
#             corrected_users["-".join(splitted)] = emails[user_first]
#         else:
#             continue
#     except Exception:
#         if not splitted[0] in corrected_users:
#             corrected_users[splitted[0]] = emails[user_first]
#
# out = open("new_data.json", "w")
# out.write(json.dumps(corrected_users, indent=1))
# print(len(emails))
# print(count)
