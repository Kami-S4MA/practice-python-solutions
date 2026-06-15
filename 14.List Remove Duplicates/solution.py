def removeDuplicate(l):
  print(list(set(l)))

def removeDuplicateLoop(l):
  a = []
  for i in l:
    if i not in a:
      a.append(i)
  
  print(a)

a = eval(input("Enter List: "))

removeDuplicate(a)
removeDuplicateLoop(a)