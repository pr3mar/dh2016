import os, json

emails = {}
for dir in os.listdir("emails_by_address"):
    start = dir.find("from_")
    if start == -1:
        start = dir.find("to_")
        end = dir.find("@", start + 3)
        receiver = dir[start + 3:end]
    else:
        end = dir.find("@", start + 5)
        receiver = dir[start + 5:end]

    if not(receiver in emails):
        emails[receiver] = {}

    with open("emails_by_address/" + dir) as email:
        for line in email:
            start = line.find("maildir/")
            end = line.find("/", start + 8)
            sender = line[start + 8:end]
            if not (sender in emails[receiver]):
                # print("\t+ " + sender)
                emails[receiver][sender] = 1
            else:
                # print("\t+++ " + sender)
                emails[receiver][sender] += 1


print(json.dumps(emails, indent=1))
print(len(emails))
