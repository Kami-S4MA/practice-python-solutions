file = open("primes.txt") 
primes = set(int(line.strip()) for line in file)

file = open("happy.txt") 
happy = set(int(line.strip()) for line in file)

overlap = []

for a in primes:
    if a in happy:
        overlap.append(a)

print(set(overlap))