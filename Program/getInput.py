from conversion import*
def getInput(choice):
    inputData = []
    
    #for Decimal Input
    if(choice.lower() == "d"):
        validDecimalInput = False
        while(not validDecimalInput):
            firstNumber =  input("Enter the first decimal number:")
            if(isValidDecimalInput(firstNumber)):
                if(int(firstNumber) < 0 or int(firstNumber) > 255):
                    print("**Error!** Please enter the decimal number between 0 and 255!")
                    continue
            else:
                continue
            secondNumber =  input("Enter the second decimal number:")
            if(isValidDecimalInput(secondNumber)):
                if(int(secondNumber) < 0 or int(secondNumber) > 255):
                    print("**Error!** Please enter the decimal number between 0 and 255!")
                    continue
            else:
                continue
            input1 = int(firstNumber)
            input2 = int(secondNumber)
            if ((input1 + input2) > 255):
                print("**Error!** Enter decimal numbers having sum less than 255!")
            else:                
                inputData.append(input1)
                inputData.append(input2)
                validDecimalInput = True
        return inputData
    
    #for Binary Input
    elif(choice.lower() == "b"):
        ValidBinaryInput = False
        while(ValidBinaryInput == False):
                number1 = input("Enter the first binary number:")
                if(isValidBinaryInput(number1)):
                    if(convertToDecimal(number1) < 0 or convertToDecimal(number1) > 255):
                        print("\n**Error!** Please enter valid 8 digit binary number.")
                        continue
                else:
                    print("Please enter a valid binary number!")
                    continue
                number2 = input("Enter the second binary number:")
                if(isValidBinaryInput(number2) ):
                    if(convertToDecimal(number2) < 0 or convertToDecimal(number2) > 255):
                        print("\n**Error!** Please enter valid 8 digit binary number:")
                        continue
                else:
                    print("Please enter a valid binary number:")
                    continue
                if(convertToDecimal(number1) + convertToDecimal(number2)) > 255:
                    print("**Error!** Enter binary numbers having sum less than 11111111.")
                else:
                    inputData.append(split(number1))
                    inputData.append(split(number2))
                    ValidBinaryInput = True
        return inputData
    
#split function 
def split(word):
    return[int(char) for char in word]

#checking valid decimal input
def isValidDecimalInput(number):
    try:
        int(number)
        return True
    except:
        if(number == ""):
            print("**Error!** You have not entered any input")
            return False
        else:
            print("**Error!** Please, do not enter the float and alphabetical value!")
            return False
        
#checking valid binary input
def isValidBinaryInput(input):
    try:
        for i in input:
            if(i not in ["0","1"]):
                print("**Error!** Please enter a valid binary number!")
                return False
    except:
           if(number == ""):
                print("**Error!** Do not enter empty field!")
                return False
           else:
               print("**Error!** Please, do not enter the float and alphabetical value!")
               return False
    return True
