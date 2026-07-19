import random

def cowsAndBulls():
  a = {}
  c = 0
  l = []
  m = 0

  while m != 4:
    x = random.randint(1,9)
    if x not in l:
      m += 1
      a[x] = m
      l.append(x)

  while  True:

    if c == 4:
      print("\nYou have guessed correctly!")

      if input("\nDo you want to play again? (Y/n): ").lower() == "y":
        cowsAndBulls()
      else:
        print("GOODBYE!")
        break

    else:
      c = 0
      b = 0
      n = 0
      for i in input("\nEnter your guess: "):
        n += 1

        if int(i) in a.keys():
          if a[int(i)] == n:
            c += 1
          else:
            b += 1
      print(c, "cows,", b, "bulls")

cowsAndBulls() 