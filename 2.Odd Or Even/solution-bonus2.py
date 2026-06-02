a = int(input("Enter divident: "))
b = int(input("Enter divisor: "))

if not b:
  print(a,"cannot be divided by 0")
elif a % b:
  print(b,"does not divide",a,"evenly")
else:
  print(int(a/b))