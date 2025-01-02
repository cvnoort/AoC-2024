#!/usr/bin/python3 

################################### part 1 ###################################

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

################################### part 2 ###################################

price_dict = {}
for secret_number in initial_numbers:
    price_changes = []
    buyer_dict = {}
    # Get prices/price changes for a buyer's set of secret numbers
    for i in range(2000):
        prev_number = secret_number
        secret_number = get_next_secret_num(secret_number)
        price = str(secret_number)[-1]
        change = int(str(prev_number)[-1]) - int(price)
        price_changes.append(change)
        if len(price_changes) > 4:
            price_changes.pop(0)
            buyer_dict.setdefault(str(price_changes), int(price))
    # Update total bananas for each sequence of four price changes
    for sequence in buyer_dict:
        price_dict.setdefault(sequence, 0)
        price_dict[sequence] += buyer_dict[sequence] 
    
print("Maximum number of bananas:", 
      price_dict[max(price_dict.keys(), key=(lambda k: price_dict[k]))]) 
