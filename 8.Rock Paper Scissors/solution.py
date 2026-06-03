def RockPaperScissors():
  print("\nChoices: \n 1 = Rock \n 2 = Paper \n 3 = Scissors\n")

  beats = {
    1: 3,
    2: 1,
    3: 2
  }

  choice1 = int(input("Player1 Choice: "))
  choice2 = int(input("Player2 Choice: "))

  if choice1==choice2: print("\nIts a Draw!!!")
  elif choice1 == beats[choice2]: print("\nPlayer2 wins!!!")
  else: print("\nPlayer1 wins!!!")

  # retry logic
  if input("\nDo you want to play again?[y/N]: ").lower() == "y":
    RockPaperScissors()
  else:
    print("\nJust as I thought NOOBS")

RockPaperScissors()    
