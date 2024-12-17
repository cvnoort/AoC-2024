#!/usr/bin/python3

with open("input.txt") as file: 
    disk_map = file.read().strip()

disk_list = sum([[i/2] * int(block_size) if i % 2 == 0 
                 else ["."] * int(block_size) 
                 for i, block_size in enumerate(disk_map)], [])

for i in range(len(disk_list)-1, -1, -1):
    if disk_list[i] != ".":
        dest = disk_list.index(".")
        if dest < i:
            disk_list[dest], disk_list[i] = disk_list[i], disk_list[dest]
        else: 
            break

check = [i * file_id for i, file_id in enumerate(disk_list) if file_id != "."]
checksum = int(sum(check))

print("Filesystem checksum:", checksum)
