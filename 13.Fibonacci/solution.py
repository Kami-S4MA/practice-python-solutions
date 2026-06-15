def fibonacci(n):
  if n == 1:
    print("1")
  elif n == 0:
    print("")
  else:
    a = 1
    b = 1
    s = [1,1]

    for i in range(n-2):
      c = a + b
      s.append(c)

      a,b = b,c
    print(" ,".join(str(x) for x in s))

fibonacci(int(input("Enter number: ")))