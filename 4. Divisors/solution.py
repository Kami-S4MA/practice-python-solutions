a = int(input("Enter a number: "))
print("The divisors of this number are:", ", ".join([str(i+1) for i in range(a) if (not a % (i+1))]))