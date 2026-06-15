a = int(input("Enter a number: "))

print("Numbers less than 10 are:", [x for x in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if x < a])