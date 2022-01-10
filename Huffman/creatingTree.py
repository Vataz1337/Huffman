from Huffman.readfile import *

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

#def printEncodedMessageKey(node,  val=''):
#    newVal = val + str(node.huff)
#    if (node.left):
#        printEncodedMessageKey(node.left, newVal)
#    if (node.right):
#        printEncodedMessageKey(node.right, newVal)
#    if (not node.left and not node.right):
#        print(f"{newVal}", end='')

def getEncodedMessageKeyToFile(node,filename, val=''):
    file = open(filename,"a")
    newVal = val + str(node.huff)
    if (node.left):
        getEncodedMessageKeyToFile(node.left,filename, newVal)
    if (node.right):
        getEncodedMessageKeyToFile(node.right,filename, newVal)
    if (not node.left and not node.right):
        file.write(str(newVal))

def getEncodedMessageKeyToDictionary(node, dictionary, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        getEncodedMessageKeyToDictionary(node.left, dictionary, newVal)
    if (node.right):
        getEncodedMessageKeyToDictionary(node.right, dictionary, newVal)
    if (not node.left and not node.right):
        dictionary[str(node.symbol)] = str(newVal)

chars = getting_keys(count_frequency(readtxt('data.txt')))
freq = getting_values(count_frequency(readtxt('data.txt')))
nodes = []

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huff = 0
    right.huff = 1

    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

