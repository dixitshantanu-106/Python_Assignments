import math
def readMatrix(name):
    myfile = open(name, 'r')
    data = myfile.read()
    myfile.close()
    array = []
    num = ""
    for i in data:
        if i == ' ' or i == '\n':
            array.append(num)
            num = ""
        else:
            num += i
    else:
        array.append(num)
    return array

def writeMatrix(array, name):
    n = int(math.sqrt(len(array)))
    myfile = open(name, 'w')
    for i in range(len(array)):
        if i % n == 0 and i != 0:
            myfile.write('\n')
        myfile.write(array[i] + " ")
    myfile.close()
    return
