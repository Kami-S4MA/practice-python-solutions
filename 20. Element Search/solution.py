def bSearch(l,n):
  a = 0
  b = len(l) - 1
  mid = (a + b)//2
  
  while a <= b:
    if l[mid] == n:
      return 1
    elif l[mid] > n:
      b = mid - 1
      mid = (a + b)//2
    else:
      a = mid + 1
      mid = (a + b)//2

  return 0

print(bSearch(eval(input("Enter list: ")),int(input("Enter number: "))))   


        
