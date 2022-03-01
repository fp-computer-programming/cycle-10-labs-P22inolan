# Author: IBN (AMDG) 1/27/2022
def sum_numbers(num):
    total = 0 # blank total
    count = 0 # counter for numbers
    while count <= num: # while the count is less than or equal to the input:
        total += count # add count number to total
        count += 1 # increase count by 1 every time
    return total

print(sum_numbers(10))
print(sum_numbers(12))
