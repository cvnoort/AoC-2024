#!/usr/bin/python3

import numpy as np

with open("input.txt") as file:
    lab_map = np.array( [list(line.strip("\n")) for line in file] )

# Initiate guard coordinates
guard_start = np.argwhere(lab_map == "^")[0]
guard_x = guard_start[1]
guard_y = guard_start[0]

while guard_y in range(0,len(lab_map)-1): 

    # Mark unique position 
    if lab_map[guard_y][guard_x] != "X":
        lab_map[guard_y][guard_x] = "X"

    # Move forward or rotate if there is an obstacle ahead
    if guard_y == 0:
        #print("Leaving the area")
        break
    elif lab_map[guard_y-1][guard_x] == "#":
        #print("Obstacle!")
        old_x = guard_x
        old_y = guard_y
        lab_map = np.rot90(lab_map)
        guard_x = old_y
        guard_y = len(lab_map) - old_x - 1
    else:
        #print("Moving ahead")
        guard_y -= 1

print("Number of distinct positions visited by guard:", (lab_map == "X").sum())
