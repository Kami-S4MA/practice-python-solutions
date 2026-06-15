import random

c = True

while c:
  a = random.randint(1,9)
  s = 0

  while True:
    b = int(input("\nEnter a number: "))

    if b == a:
      print("Your guess was correct!!")
      break
    elif b > a:
      print("Your guess was high.")
      s += 1
    else:
      print("Your guess was low.")
      s += 1

  print("\nYou have guessed after",s,"tries.")
  
  if input("Do you wish to continue(Y/n): ").lower() != "y":
    print("Goodbye")
    c = False
  
  
