import os

emails = set()
for dir in os.listdir("final_project/emails_by_address"):
    s = dir.find("from_")
    if s == -1:
        s = dir.find("to_")
        e = dir.find("@", s + 3)
        emails.add(dir[s + 3:e])
    else:
        e = dir.find("@", s + 5)
        emails.add(dir[s + 5:e])

    with open("final_project/emails_by_address/"+dir) as email:
        for line in email:
            s = line.find("maildir/")
            e = line.find("/", s+8)
            emails.add(line[s+8:e])


print emails
print len(emails)