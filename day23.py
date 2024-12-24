#!/usr/bin/python3 

################################### part 1 ###################################

with open("input.txt") as file: 
    connections = [line.strip("\n").split("-") for line in file]

conn_dict = {}

for connection in connections:
    conn_dict[connection[0]] = ([connection[1]] 
                                if connection[0] not in conn_dict 
                                else conn_dict[connection[0]] + [connection[1]])
    conn_dict[connection[1]] = ([connection[0]] 
                                if connection[1] not in conn_dict 
                                else conn_dict[connection[1]] + [connection[0]])


triangles = []

for i, connection in enumerate(connections):
    if any(computer.startswith("t") for computer in connection):
        triangles.extend([tuple(sorted((connection[0], connection[1], c))) 
                         for c in conn_dict[connection[0]] 
                         if c in conn_dict[connection[1]]])

print('There are', len(set(triangles)), 
      'sets of thee connected computers where at least one starts with "t".')

################################### part 2 ###################################

parties = []

for computer in conn_dict:
    party = [computer]
    for comp in conn_dict[computer]:
        if all(c in conn_dict[comp] for c in party):
            party.append(comp)
    parties.append(party)

print('The password for the LAN party is:',
      ",".join(sorted(max(parties, key=len))))
