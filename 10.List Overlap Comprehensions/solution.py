import random

a = [random.randint(1,30) for i in range(random.randint(20,50))]
b = [random.randint(1,30) for i in range(random.randint(20,50))]

print(a)
print(b)

# s = {}

# for i in a:
#   s[i] = 0

# a = []

# for i in b:
#   if i in s and not s[i]:
#     a.append(i)

# print(a)

seen = {}

print([(seen.update({x: x})) or x for x in a if x in b and x not in seen ])
