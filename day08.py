#!/usr/bin/python3

import numpy as np

with open("input.txt") as file: 
    antennae = np.array( [list(line.strip("\n")) for line in file] )

antinodes = []

for i, antenna in np.ndenumerate(antennae):
    if antenna != ".":

        for j, other in np.ndenumerate(antennae):
            if other == antenna and j != i:

                distance = (j[0] - i[0], j[1] - i[1])

                antinode_1 = (j[0] - 2 * distance[0], j[1] - 2 * distance[1])
                antinode_2 = (i[0] + 2 * distance[0], i[1] + 2 * distance[1])

                for antinode in [antinode_1,antinode_2]:
                    if (antinode[0] in range(len(antennae[0])) 
                            and antinode[1] in range(len(antennae[1]))):
                        antinodes.append(antinode)

print("Number of unique locations that contain an antinode:", len(set(antinodes)))
