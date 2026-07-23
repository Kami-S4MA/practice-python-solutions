file = open("names.txt", "r")
counts = {}

for l in file:
    a = l.strip()  

    if a in counts:
        counts[a] += 1
    else:
        counts[a] = 1

for a, b in counts.items():
    print(a,":",b)