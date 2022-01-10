#import operator
from Huffman.creatingTree import *

#def readBytes(filename):
#    bytes = []
#    with open(filename, 'rb') as file:
#        while True:
#            b = file.read(1)
#            if not b:
#                break
#            bytes.append(int.from_bytes(b, byteorder='big'))
#    return bytes


#outbytes = randomBytes(10)
#print(outbytes)
#displayBytes(outbytes)
#
#filename = 'binaryFile.txt'
#writeBytes(filename, outbytes)
#
#inbytes = readBytes(filename)
#displayBytes(inbytes)
#print(f'Match: {operator.eq(outbytes, inbytes)}')

def segregateIntoBytes():
    f = open('prebin.txt', 'r')
    mytext = f.read()
    result = []
    for i in range(0, len(mytext), 8):
        result.append(mytext[i: i + 8])
    #print(result)
    last_elem = result[len(result) - 1]
    last_elem_length = len(last_elem)
    if last_elem_length != 8:
        bitsToIgnore = 8 - last_elem_length
        bitsToIgnoreInbin = decimalToBinary(bitsToIgnore)
        if len(bitsToIgnoreInbin) < 3:
            while len(bitsToIgnoreInbin) != 3:
                bitsToIgnoreInbin = "0" + bitsToIgnoreInbin
        for i in range(bitsToIgnore):
            result[len(result)-1] = result[len(result)-1].__add__("0")
        #print(result)
        #print(bitsToIgnoreInbin)
    else:
        bitsToIgnoreInbin = "000"
    with open('readyToBeConverted.txt', 'w') as file:
        file.write(bitsToIgnoreInbin)
        for i in result:
            iconverted = str(i)
            file.write(iconverted)
    return result

def saveAsBinaryFile(listOfBinary):
    with open('binaryFile.txt', 'wb') as fbinary:
        for i in listOfBinary:
            i = binaryToDecimal(i)
            fbinary.write(i.to_bytes(1, byteorder='big'))

def saveToPrebin():
    f = open('data.txt', 'r')
    mytext = f.read()
    datatxt = str(mytext)
    prebinf = open("prebin.txt", "w")
    for letter in datatxt:
        for key in dictorany.keys():
            if key == letter:
                prebinf.write(dictorany[key])

def decimalToBinary(n):
    return str(bin(n).replace("0b", ""))

def binaryToDecimal(n):
    return int(n,2)

def saveTree():
    with open('tree.txt', 'w') as file:
        for key in dictorany.keys():
            asciiNumebr = (ord(key))
            file.write("0" + str(decimalToBinary(asciiNumebr)))
            file.write(dictorany[key])



printNodes(nodes[0])
dictorany = {}
getEncodedMessageKeyToDictionary(nodes[0], dictorany)
saveToPrebin()
saveTree()
saveAsBinaryFile(segregateIntoBytes())



