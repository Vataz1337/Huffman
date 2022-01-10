#import operator
from Huffman.creatingTree import *

#print(f'Match: {operator.eq(outbytes, inbytes)}')

def segregateIntoBytes():
    f = open('prebin.txt', 'r')
    mytext = f.read()
    result = []
    for i in range(0, len(mytext), 8):
        result.append(mytext[i: i + 8])
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
    else:
        bitsToIgnoreInbin = "000"
    result.insert(0,bitsToIgnoreInbin)
    numOfkeys = len(dictorany.keys())
    numOfkeysBin = decimalToBinary(numOfkeys)
    result.insert(1,numOfkeysBin)
    all_values = freq
    max_value = max(all_values)
    max_value_bin = decimalToBinary(max_value)
    max_value_bin_len = (len(max_value_bin))
    max_value_bin_len = decimalToBinary(max_value_bin_len)
    #if len(max_value_bin)>8:
    #    splitNumbers = []
    #    timesDevided = len(max_value_bin) / 8
    #    timesDevided = round(timesDevided)
    #    if(len(max_value_bin)%2==0):
    #        for i in range(timesDevided):
    #            splitNumbers.append(max_value/timesDevided)
    #        timesDevidedBin = decimalToBinary(timesDevided)
    #    else:
    result.insert(2, max_value_bin_len)
    i = 2
    dictionary2 = dict(zip(chars, freq))

    for key in dictionary2.keys():
        asciiNumebr = (ord(key))
        i = i + 1
        lengthOfAscii = len(str(decimalToBinary(asciiNumebr)))
        if lengthOfAscii < 8:
            zerosToAdd = 8 - lengthOfAscii
            result.insert(i, (zerosToAdd * "0" + str(decimalToBinary(asciiNumebr))))

        value = decimalToBinary(dictionary2[key])
        if len(value) < len(max_value_bin):
            while len(value) != len(max_value_bin):
                value = "0" + value
        result.insert(i+1, value)
        i = i+1
    print(result)
    return result

def saveAsBinaryFile(listOfBinary):
    with open('binaryFile.txt', 'wb') as fbinary:
        for i in listOfBinary:
            i = binaryToDecimal(i)
            fbinary.write(i.to_bytes(1, byteorder='big'))

def readBytes(filename):
    bytes = []
    with open(filename, 'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))
    return bytes

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


printNodes(nodes[0])
dictorany = {}
getEncodedMessageKeyToDictionary(nodes[0], dictorany)
saveToPrebin()
saveAsBinaryFile(segregateIntoBytes())



