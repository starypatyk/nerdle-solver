from all_perms_file import all_perms
from libnerdle import *

guess = '58-46=12'
test_perms = all_perms

while True:
    print("Enter guess:    " + guess)
    answers = calculate_answers(guess, test_perms)
    hint = input("Enter response: ")
    test_perms = answers[hint]
    if (len(test_perms) == 1):
        print("Enter guess:    " + test_perms[0] + " - for sure ;-)")
        break
    else:
        guess = calculate_best_guess(test_perms)
