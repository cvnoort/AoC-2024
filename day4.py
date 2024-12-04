#!/usr/bin/python3

import numpy as np

with open("input.txt") as file: 
    xmas_array = np.array( [list(line.strip("\n")) for line in file] )

xmas = "XMAS"
xmas_total = 0

def find_xmas(xmas_list):
    xmas_count = 0
    for i in range(len(xmas_list)-3):
        if "".join(xmas_list[i:i+len(xmas)]) == xmas:
            xmas_count += 1
    return xmas_count

# Find horizontal and vertical instances of XMAS

for i in range(len(xmas_array)):

    xmas_total += find_xmas(xmas_array[i])
    xmas_total += find_xmas(np.rot90(xmas_array,1)[i])
    xmas_total += find_xmas(np.rot90(xmas_array,2)[i])
    xmas_total += find_xmas(np.rot90(xmas_array,3)[i])

# Find diagonal instances of XMAS

for i in range(-len(xmas_array)+4,len(xmas_array)-3):

    xmas_diag = np.diag(xmas_array, i)
    xmas_total += find_xmas(xmas_diag)
    xmas_total += find_xmas(xmas_diag[::-1])

    xmas_diag_rl = np.diag(np.fliplr(xmas_array), i)
    xmas_total += find_xmas(xmas_diag_rl)
    xmas_total += find_xmas(xmas_diag_rl[::-1])

print("Total number of instances of XMAS:", xmas_total)
