import random

def passGen():
  a = "abcdefghijklmnopqrstuvwxyz"
  s = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
  b = ["galaxy", "whisper", "anchor", "bicycle", "vortex","cactus", "shadow", "melody", "lantern", "glacier", "puzzle", "harvest", "safari", "echo", "compass", "thunder", "velvet", "horizon", "beacon", "oasis"]
  c = ""
  d = []

  if input("\nDo you want a strong password? (Y/n): ").lower() == "y":
    for i in range(random.randint(15,40)):

      if random.randint(0,1):
        if random.randint(0,1):
          c = c + a[random.randint(0,25)]
        else:
          c = c + a[random.randint(0,25)].upper()

      elif random.randint(0,1):
        c = c + s[random.randint(0,31)]

      else:
        c = c + str(random.randint(0,9))

  else:
    for i in range(random.randint(4,7)):
      if random.randint(0,1):
        c = c + b[random.randint(0,19)]

      elif random.randint(0,1):
        c = c + s[random.randint(0,31)]

      else:
        c = c + str(random.randint(0,9))
  
  if c not in d:
    d.append(c)
    print("\nYour password is", c)
    if input("Do you want another password? (Y/n): ").lower() == "y":
      passGen()

    else:
      print("\nGOODBYE!")
passGen()   
