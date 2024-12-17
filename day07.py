#!/usr/bin/python3

import re

with open("input.txt") as file: 
    cal_equations = []
    for line in file:
        cal_equations.append(line.strip().split(": "))


success_results = []

for calibration in cal_equations:

    test_val = float(calibration[0])

    # Write equation using + at each operator position
    # (note brackets to ensure left-to-right evaluation)
    equation = "(" + calibration[1].replace(" ", ")+") + ")"
    operator_count = equation.count("+")
    equation = "(" * operator_count + equation
    
    # Get indices of the operator positions
    operators = [i.start() for i in re.finditer("\+", equation)]

    # Create max binary number to represent operator positions
    op_bin = "0b" + "1" * operator_count
    
    # Iterate over each binary number up to the max defined above
    for ob in range(int(op_bin, 2) +1):
        
        ob_list = list(bin(ob)[2:].rjust(len(op_bin[2:]), "0"))

        current_eq = equation

        # Replace + operator with * operator at indices that correspond to a 1
        for operator_pos in zip(ob_list, operators):
            if operator_pos[0] == "1":
                current_eq = list(current_eq)
                current_eq[operator_pos[1]] = "*"
                current_eq = "".join(current_eq)

        # Evaluate the resulting equation and compare to the test value
        if eval(current_eq) == test_val:
            success_results.append(test_val)
            break

print("Total calibration result:", int(sum(success_results)))
