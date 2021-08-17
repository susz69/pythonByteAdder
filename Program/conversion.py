#conversion
def convertToDecimal(number):
    decimalNumber = 0
    i = 0
    for j in range(len(number)-1,-1,-1):
        decimalNumber += int(number[j]) * (2**i)
        i += 1
    return decimalNumber
        
def convertToBinary(number):
    reversedBinaryList = []
    binaryList = []
    if(number == 0):
        binaryList.append(0)
    else:
        while(number != 0):
            r = number % 2
            reversedBinaryList.append(r)
            number //= 2
    for i in range(len(reversedBinaryList)-1,-1,-1):
        binaryList.append(reversedBinaryList[i])
    eightBitBinaryList = eightBit(binaryList)    
    return eightBitBinaryList

def eightBit(binaryList):
    if(len(binaryList)!= 8):
        for i in range(len(binaryList),8):
            binaryList.insert(0,0)
    return binaryList

