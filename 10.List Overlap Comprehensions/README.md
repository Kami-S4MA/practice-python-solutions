# Problem 10: List Overlap Comprehensions

**Problem link: [here](https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html)**

## Problem Statement

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

```bash
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

- Randomly generate two lists to test this

## Example

Output:

```bash
[10, 15, 30, 17, 19, 29, 22, 1, 10, 26, 25, 12, 16, 18, 4, 5, 30, 10, 5, 10, 10, 14, 5, 2, 5, 29, 26, 16, 10, 13, 8, 20, 9, 4, 29, 1, 30, 21, 1, 29, 11]
[19, 14, 13, 5, 29, 24, 19, 25, 27, 2, 28, 5, 17, 14, 25, 30, 2, 6, 2, 2, 19, 18, 18]
[19, 14, 13, 5, 29, 19, 25, 2, 5, 17, 14, 25, 30, 2, 2, 2, 19, 18, 18]
```
