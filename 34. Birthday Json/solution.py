import json

f = open("Bdays.json", "r+")

Bdays = json.load(f)

name = input("Whose Birthday do you want to know?: ").lower()

if name in Bdays:
    print("The Birthday is", Bdays[name])

else:
    if input("This name is not in the dictionary!\n\nWould you like to add this to the dictionary?(Y/n): ").lower() == "y":
        Bdays[name] = input("Enter the Birthday(MM/DD/YYYY): ")

        f.seek(0)
        json.dump(Bdays, f, indent = 4)
        f.truncate()

        print("Added Successfully")

    else:
        print("Goodbye!")