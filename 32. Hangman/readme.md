# Problem 32: Hangman

**Problem link: [here](https://www.practicepython.org/exercise/2017/01/10/32-hangman.html)**

## Problem Statement

This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

- Only let the user guess 6 times, and tell the user how many guesses they have left.
- Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

Optional additions:

- When the player wins or loses, let them start a new game.
- Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!


## Example

Output:

```bash
_ _ _ _ _ _ _ _  

Enter your guess: a
incorrect guess.

Enter your guess: q
incorrect guess.

Enter your guess: w
incorrect guess.

Enter your guess: g

Correct!
_ _ _ G _ _ _ G  

Enter your guess: i

Correct!
_ I _ G _ _ _ G  

Enter your guess: l
incorrect guess.

Enter your guess: n

Correct!
_ I N G _ _ N G  

Enter your guess: r
incorrect guess.

Enter your guess: f
incorrect guess.

Enter your guess: g
Letter already guessed!

Enter your guess: h
incorrect guess.

Enter your guess: v
incorrect guess.

Enter your guess: p

Correct!
P I N G P _ N G  

Enter your guess: o

Correct!
P I N G P O N G  

You won!!
The word was: PINGPONG
Would you like to play again? (Y/n): n
```

