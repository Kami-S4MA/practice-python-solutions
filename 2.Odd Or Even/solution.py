num = int(input("Please enter a number: "))

print("The number is " + ("divisible by 4" if not num%4 else("odd" if num%2 else "even")))
