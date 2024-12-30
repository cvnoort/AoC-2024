#!/usr/bin/python3 

def mix(number:int, operation:str) -> int:
    "Mix a new number into the secret number."
    new_number = eval(f"{number} {operation}")
    return number ^ int(new_number)

def prune(number:int) -> int:
    "Prune the new secret number."
    return number % 16777216

def get_next_secret_num(number:int) -> int:
    "Get next secret number by mixing and pruning."
    step_1 = prune(mix(number,"* 64"))
    step_2 = prune(mix(step_1,"/ 32"))
    step_3 = prune(mix(step_2,"* 2048"))
    return step_3


with open("input.txt") as file: 
    initial_numbers = [int(line.strip("\n")) for line in file]


twothousandth_numbers = []
for secret_number in initial_numbers:
    for i in range(2000):
        secret_number = get_next_secret_num(secret_number)
    #print(secret_number)
    twothousandth_numbers.append(secret_number)

print("Sum of 2000th secret number for each buyer:", 
      sum(twothousandth_numbers))
