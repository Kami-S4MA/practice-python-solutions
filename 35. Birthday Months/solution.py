import json

f1 = open("Bdays.json", "r")
f2 = open("months.json", "w")

Bdays = json.load(f1)

monthNames = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = {}

for i in Bdays:

    if monthNames[int(Bdays[i][0:2])-1] not in months:
        months[monthNames[int(Bdays[i][0:2])-1]] = 1

    else:
        months[monthNames[int(Bdays[i][0:2])-1]] += 1

json.dump(months, f2, indent = 4)

