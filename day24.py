#!/usr/bin/python3

class Wire:

    def __init__(self, name, wire_val):
        self.name = name
        self.wire_val = wire_val

class Gate:

    def __init__(self, logic:str, input_1:str, input_2:str):
        self.logic = logic
        self.input_1 = input_1
        self.input_2 = input_2
        
    def get_output(self, wire_dict:dict) -> str:
        if self.logic == "AND":
            return ("1" if wire_dict[self.input_1].wire_val == "1" 
                    and wire_dict[self.input_2].wire_val == "1" 
                    else "0")
        elif self.logic == "OR":
            return ("1" if wire_dict[self.input_1].wire_val == "1" 
                    or wire_dict[self.input_2].wire_val == "1" 
                    else "0")
        elif self.logic == "XOR":
            return ("1" if wire_dict[self.input_1].wire_val 
                    != wire_dict[self.input_2].wire_val 
                    else "0")


with open("input.txt") as file: 
    wires = {}
    gates = {}
    for line in file:
        line = line.strip()
        if ":" in line:
            wires[line.split(": ")[0]] = Wire(line.split(": ")[0], 
                                              line.split(": ")[1]) 
        elif "->" in line:
            gates[line.split()[4]] = Gate(line.split()[1], 
                                          line.split()[0], line.split()[2])

while any(gate not in wires for gate in gates):
    for gate in gates:
        if (gates[gate].input_1 in wires.keys() 
                and gates[gate].input_2 in wires.keys()):
            out_val = gates[gate].get_output(wires)
            wires[gate] = Wire(gate, out_val)

z_wires = sorted([wires[wire].name for wire in wires 
                  if wires[wire].name.startswith("z")])
z_bits = "".join([wires[z].wire_val for z in z_wires[::-1]])

print('Decimal number output on the wires starting with "z":', int(z_bits, 2))
