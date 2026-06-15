a = int(input("Enter a number: "))
b = 0

for i in range(2,a):
  if not a % i:
    b = 1
    break

if b:
  print(a,"is not a prime number.")
else:
  print(a,"is a prime number.")

