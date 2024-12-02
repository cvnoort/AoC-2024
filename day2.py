#!/usr/bin/python3

def check_report(report):

    direction = "unknown"

    for i, level in enumerate(report[1:], start=1):

        if abs(level - report[i-1]) not in range(1,4):
            safe = False
            break

        if level > report[i-1]:
            if direction == "decreasing":
                safe = False 
                break
            direction = "increasing"
        elif level < report[i-1]:
            if direction == "increasing":
                safe = False 
                break
            direction = "decreasing"

        safe = True
    
    return safe

with open("input.txt") as file: 
    safe_checks = []
    for line in file:
        report_vals = list(map(int, line.split())) 
        safe_checks.append(check_report(report_vals))
    
    print("Number of safe reports:", safe_checks.count(True))
