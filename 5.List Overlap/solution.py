import random

a=[random.randint(1,30) for i in range(random.randint(15,30))]
b=[random.randint(1,30) for i in range(random.randint(15,30))]
c=[]


print(a)
print(b)

seen = {}

for x in a: seen[x] = 0

for x in b:
  if x in seen and not seen[x]:
    c.append(x)
    seen[x] += 1


print(c)


