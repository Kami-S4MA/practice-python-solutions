a = input("Enter string: ")

if a.lower() == a[::-1].lower():
  print(a,"is palindrome.")
else:
  print(a,"is not palindrome.")