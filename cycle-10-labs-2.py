# Author: IBN (AMDG) 1/27/2022

def div_less(lst):
    blank = []
    for num in lst:
        if num % 5 == 0:
            if num <= 150:
                blank.append(num)
        if num > 500:
            break
    return blank

print(div_less([5, 10, 17, 160, 20]))
print(div_less([150, 75, 500, 20]))