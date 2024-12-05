#!/usr/bin/python3

with open("input.txt") as file: 
    rules = []
    updates = []
    for line in file:
        if "|" in line:
            rules.append(line.strip())
        elif "," in line:
            updates.append(line.strip())
        
rules_dict= {}
for rule in rules:
    first,second = rule.split("|")
    if first not in rules_dict.keys():
        rules_dict[first] = [second]
    else:
        rules_dict[first].append(second)


# Get all updates with pages in the correct order
updates_good = []

for update in updates:

    update_list = update.split(",")
    discard = False

    for i, page in enumerate(update_list):
        if page in rules_dict.keys():
            if True in (p in rules_dict[page] for p in update_list[:i]):
                discard = True
                break

    if discard == False:
        updates_good.append(update_list)

# Find middle page of each correctly-ordered update
middle = [int(update[int((len(update)-1)/2)]) for update in updates_good]

print("Sum of middle page numbers from all correctly-ordered updates:", sum(middle))
