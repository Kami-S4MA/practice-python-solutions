import random

file = open("sowpods.txt", "r")
words = file.read().splitlines()
print(random.choice(words))