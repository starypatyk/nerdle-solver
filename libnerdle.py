from all_perms_file import all_perms

def compare_guess(secret, guess):
    result = ['0'] * 8
    for n in range(0, 8):
        if secret[n] == guess[n]:
            result[n] = '2'
    for n in range(0, 8):
        if secret[n] != guess[n]:
            for m in range(0, 8):
                if (m != n) and (secret[n] == guess[m]) and (result[m] == '0'):
                    result[m] = '1'
                    break
    return "".join(result)

def calculate_answers(guess, test_perms):
    answers = {}

    # Check possible answers
    for n in range(0, len(test_perms)):
        perm = test_perms[n]
        result = compare_guess(perm, guess)
        if result in answers:
            answers[result].append(perm)
        else:
            answers[result] = [ perm ]

    return answers

def calculate_best_guess(test_perms):

    min_max_bucket = 20000
    best_next_guess = ''

    for n in range(0, len(all_perms)):

        guess = all_perms[n]
        answers = calculate_answers(guess, test_perms)

        # Calculate largest bucket for this guess
        max_bucket = 0
        for _, bucket in answers.items():
            num = len(bucket)
            if num > max_bucket:
                max_bucket = num

        # Select guess having smallest largest bucket ;-)
        if max_bucket < min_max_bucket:
            min_max_bucket = max_bucket
            best_next_guess = guess

    return best_next_guess
