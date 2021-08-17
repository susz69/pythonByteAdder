#adder file
from conversion import*
from gates import*

#8-bit adder model implementation
def adder(binaryList):
    binaryNumber1 = binaryList[0]
    binaryNumber2 = binaryList[1]
    carry = 0
    reverseSum = []
    binarySum = []
    print("\n")
    print("*-------------------------*")
    print("| Adding in binary method |")
    print("*-------------------------*")

    for i in binaryNumber1:
        print(i, end = " ")
    print()
    
    for i in binaryNumber2:
        print(i, end = " ")
    print()
    
    for i in range(len(binaryNumber1)-1,-1,-1):
        bit1 = int(binaryNumber1[i])
        bit2 = int(binaryNumber2[i])

        #sum operation           
        XOR = XOR_gate(bit1,bit2)
        OR = OR_gate(XOR,carry)
        NAND = NAND_gate(XOR,carry)
        Sum = AND_gate(OR,NAND)

        #carry operation
        AND1 = AND_gate(bit1,bit2)
        AND2 = AND_gate(XOR,carry)
        carry = NOT_gate(NOR_gate(AND1,AND2))

        reverseSum.append(Sum) 

    for i in range(len(reverseSum)-1,-1,-1):
        binarySum.append(reverseSum[i])
    return binarySum
