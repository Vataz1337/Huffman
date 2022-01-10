def readtxt(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        return data

def count_frequency(data):
    all_freq = {}
    for i in data:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def getting_keys(dict):
    keyList = []
    for key in dict.keys():
        keyList.append(key)
    return keyList

def getting_values(dict):
    valueList = []
    for value in dict.values():
        valueList.append(value)
    return valueList


