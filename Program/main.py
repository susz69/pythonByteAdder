#importing files for accessing methods and values in main file
from getInput import*
from adder import*

#main function
def main():
    #decoration
    print(" ############################################## ~~~Python~~~ #################################################")
    print("##                                                                                                           ##")
    print("##   888888       BBBBBBB  IIIIIIII TTTTTTTTTT         AA       DDDDDDDD    DDDDDDDDD     EEEEEEEE RRRRRRR   ##")
    print("##  88    88      BB    BB    II        TT            AAAA         DD    DD     DD    DD  EE       RR    RR  ##")
    print("##  88    88      BB    BB    II        TT           AA  AA        DD     DD    DD     DD EE       RR    RR  ##")
    print("##   888888  ==== BBBBBBB     II        TT          AA    AA       DD     DD    DD     DD EEEEEE   RRRRRR    ##")
    print("##  88    88      BB    BB    II        TT         AAAAAAAAAA      DD     DD    DD     DD EE       RR  RR    ##")
    print("##  88    88      BB    BB    II        TT        AA        AA     DD    DD     DD    DD  EE       RR    RR  ##")
    print("##   888888       BBBBBBB  IIIIIIII     TT       AA          AA DDDDDDDD    DDDDDDDDD     EEEEEEEE RR     RR ##")
    print("##                                                                                                           ##")
    print(" ######################################## ~.~ By Susan Shrestha ~.~ ##########################################")
    print("")
    
    flag=False
    while(flag==False):
        #getting choice from user
        print("*-------------------------------------------------------*")
        choice = input("| Enter d/D for decmial number and b/B for binary number |\n*-------------------------------------------------------*\n")
        if(choice.lower() == "d"):
            decimalMethod()            
        elif(choice.lower() == "b"):
            binaryMethod()
        else:
            print("Please enter a valid choice!")
            continue       
        correctInput = False
        while(correctInput == False):
            print("\n")
            print("*-------------------------------------*")
            exitprogram = input("| Type 'c' to Continue or 'e' to Exit: |\n*-------------------------------------*\n")
            if(exitprogram.lower()=="e"):
                flag = True
                correctInput = True
            elif(exitprogram.lower() == "c"):
                flag = False
                correctInput = True
            else:
                print("Please enter a valid choice!")

#for decimal addition                 
def decimalMethod():
    binaryNumberList = []
    decimalNumberList = getInput("d")
    firstDecimalNumber = decimalNumberList[0]
    secondDecimalNumber = decimalNumberList[1]
    print("*--------------------------*")
    print("* Adding in decimal method *")
    print("*--------------------------*")
    print(firstDecimalNumber)
    print(secondDecimalNumber)
    pSum = firstDecimalNumber + secondDecimalNumber
    print("+")
    print(pSum)
    firstEightBitBinaryNumber = convertToBinary(firstDecimalNumber)
    secondEightBitBinaryNumber = convertToBinary(secondDecimalNumber)
    binaryNumberList.append(firstEightBitBinaryNumber)
    binaryNumberList.append(secondEightBitBinaryNumber)
    binarySum = adder(binaryNumberList)
    print("+ ")
    for i in binarySum:
        print(i ,end = " ")

#for binary addition
def binaryMethod():
    binaryNumberList = []
    binaryNumberList = getInput("b")
    binaryNumber1 = binaryNumberList[0]
    binaryNumber2 = binaryNumberList[1]
    firstEightBitBinaryNumber = eightBit(binaryNumber1)
    secondEightBitBinaryNumber = eightBit(binaryNumber2)
    binaryNumberList.append(firstEightBitBinaryNumber)
    binaryNumberList.append(secondEightBitBinaryNumber)
    binarySum = adder(binaryNumberList)
    print("+ ")
    for i in binarySum:
        print(  i, end = " ")
    print("\n")
    print("*--------------------------*")
    print("| Adding in decimal method |")
    print("*--------------------------*")
    firstDecimalNumber = convertToDecimal(binaryNumber1)
    secondDecimalNumber = convertToDecimal(binaryNumber2)
    print(firstDecimalNumber)
    print(secondDecimalNumber)
    pSum=firstDecimalNumber+secondDecimalNumber
    print("+")
    print(pSum)
    
#execution of main() function
main()













