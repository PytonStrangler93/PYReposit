def mod_checker(x, mod=0):
    return lambda y: True if y % x == mod else False


x = mod_checker(3)
print(x(3))
print(x(4))

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))  # True
