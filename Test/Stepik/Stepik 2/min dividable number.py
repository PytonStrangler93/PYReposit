x = 2423


def closest_mod_5(x):
    y = x
    if x % 5 == 0:
        return x
    else:
        while y % 5 != 0:
            y += 1
        return y


print(closest_mod_5(x))

# RECURCY


def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)

# ХЗ ЧЕ ЭТО!!!


def closest_mod_5(x):
    return x + -x % 5
