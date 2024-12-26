#!/usr/bin/python3

def convert_pins(lock_or_key:list) -> list:
    """Convert pins to a list of heights."""
    pins = [[row[pos] for row in lock_or_key] 
            for pos in range(len(lock_or_key[0]))]
    return [pin.count("#") - 1 for pin in pins]

def compare_lock_key(lock:list, key:list) -> bool:
    """Determine whether a lock/key combination fits."""
    return all(l + k < 6 for l, k in zip(lock, key))


with open("input.txt") as file: 
    locks, keys = [], []
    i_line = 1
    line_block = []
    for line in file:
        if line.strip():
            line_block.append(line.strip())
            if i_line % 7 == 0:
                if line_block[0] == "#####":
                    locks.append(line_block)
                elif line_block[0] == ".....":
                    keys.append(line_block)
                line_block = []
            i_line += 1

# Get pin heights for all locks and keys 
locks_heights = [convert_pins(lock) for lock in locks]
keys_heights = [convert_pins(key) for key in keys]

# Compare pin heights of each key to each lock 
pairs = [compare_lock_key(lock, key) 
         for key in keys_heights 
         for lock in locks_heights]

print("Unique lock/key pairs that fit together:", pairs.count(True))
