#!/usr/bin/python3

import re

with open("input.txt") as file: 
    instructions_cor = file.read()

instructions = re.findall(r"mul\(([0-9]+,[0-9]+)\)", instructions_cor)

mul_inp = [instruction.split(",") for instruction in instructions]
mul_results = [int(instruction[0]) * int(instruction[1]) for instruction in mul_inp]
mul_total = sum(mul_results)

print("Sum of all multiplications:", mul_total)
