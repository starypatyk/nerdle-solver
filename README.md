# Simple nerdle solver

Yet another simple solver for [Nerdle](https://nerdlegame.com/). Written in Python 3.

Currently this solver should solve about 69% of all nerdle puzzles in 3 attempts, the remaining ones in 4 attempts.

## Getting started

Generate list of valid nerdle solutions (equations):

```
$ python3 gen_perms.py > all_perms_file.py
```

## Finding the best initial guess

```
$ python3 gen_best_guess.py
```

This takes about 20 minutes to complete.

**Spoiler:** should return **58-46=12** as the initial guess. This guess is now hard-coded in **play.py**.

## Playing

Enter guesses as suggested by the program into **nerdle**.

Enter responses from **nerdle** as:

- black - **0** 
- purple - **1**
- green - **2**

```
$ python3 play.py
Enter guess:    58-46=12
Enter response: 10201100
Enter guess:    67*9=603
Enter response: 10101001
Enter guess:    35-6*5=5 - for sure 😉
```
