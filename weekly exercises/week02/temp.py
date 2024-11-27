# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
int_list = [1, 2, 3, 4, 5]

new_list = [x*x for x in int_list if x % 2 != 0]
print(new_list)

"""
x = list(range(3, 20, 3))
y = list(range(3,18, 3))
print(x)
print(y)
"""
for x in [1, 2, 3, 5, 6, 7, 8, 9]:
    if x % 2 == 0:
        continue
    elif x < 7:
        print(x)
    break
