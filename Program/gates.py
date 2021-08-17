#gates functions creation using bitwise operators

def AND_gate(a,b):
    return a & b

def OR_gate(a,b):
    return a | b

def XOR_gate(a,b):
    return a ^ b

def NOT_gate(a):
    return (~a) + 2

def NAND_gate(a,b):
    return NOT_gate(AND_gate(a,b))

def NOR_gate(a,b):
    return NOT_gate(OR_gate(a,b))
