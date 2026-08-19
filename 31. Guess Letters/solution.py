import random

def hangmanGame():
    file = open("sowpods.txt", "r")
    w = random.choice(file.read().splitlines())

    guessedLetters = set()
    correctLetters = set(w)

    print("_ "*len(w), "\n")

    while True:
        guess = input("Enter your guess: ").upper()

        if guess in guessedLetters:
            print("Letter already guessed!\n")
            continue

        if guess in correctLetters:
            print("\nCorrect!")
            guessedLetters.add(guess)

            display = ""

            for i in w:
                if i in guessedLetters:
                    display += i + " "
                else:
                    display += "_ "

            print(display, "\n")

        else:
            print("incorrect guess.\n")
            guessedLetters.add(guess)

        if correctLetters.issubset(guessedLetters):
            print("You won!!")
            print("The word was:", w)

            if input("Would you like to play again? (Y/n): ").lower() == "y":
                hangmanGame()
            else:
                break 

hangmanGame()