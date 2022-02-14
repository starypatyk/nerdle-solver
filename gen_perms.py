digits0 = "0123456789"
digits1 = "123456789"
opers = "+-*/"
digits_opers = "0123456789+-*/"

all_perms = []

def verify_perm(perm, ans_min, ans_max):
    val = eval(perm)
    if val >= ans_min and val < ans_max and (val == int(val)):
        all_perms.append(perm + "=" + str(int(val)))

def generate_perms(level, max_level, prev_perm, ans_min, ans_max):
    if level == 0:
        # Start with a non-zero digit
        for char in digits1:
            generate_perms(1, max_level, prev_perm + char, ans_min, ans_max)
    elif level == max_level:
        # End with a digit
        if prev_perm[-1] in opers:
            # No zero digit after an operator
            for char in digits1:
                verify_perm(prev_perm + char, ans_min, ans_max)
        else:
            # Any digit after digit
            for char in digits0:
                verify_perm(prev_perm + char, ans_min, ans_max)
    else:
        # In the middle
        if prev_perm[-1] in opers:
            # Non-zero digit after an operator
            for char in digits1:
                generate_perms(level + 1, max_level, prev_perm + char, ans_min, ans_max)
        else:
            # Anything after digit
            for char in digits_opers:
                generate_perms(level + 1, max_level, prev_perm + char, ans_min, ans_max)


generate_perms(0, 3, '', 100, 1000) # 1318 perms
generate_perms(0, 4, '', 10, 100)   # 11833 - 1318 = 10515 perms
generate_perms(0, 5, '', 0, 10)     # 17723 - 11833 = 5890 perms

print("all_perms = [")
print("  '" + "',\n  '".join(all_perms) + "'")
print("]")
