#!/usr/bin/python3

################################### part 1 ###################################

group1 = []
group2 = []

with open("input.txt") as file: 
    for line in file:
        group1.append(int(line.split()[0]))
        group2.append(int(line.split()[1]))

group1.sort()
group2.sort()

total_dist = 0

for i in range(0,len(group1)):
    dist = abs( group1[i] - group2[i] )
    total_dist += dist
    #print(i, group1[i], group2[i], dist, total_dist)

print("Total distance between the two lists:", total_dist)

################################### part 2 ###################################

similarity = [loc_id * group2.count(loc_id) for loc_id in group1]
total_sim = sum(similarity)

print("Similarity score of the two lists:", total_sim)
