import math


def getData(inFile):
    handle = open(inFile, encoding='utf8')
    numbers = list()
    correct = 0
    incorrect = 0

    for line in handle:
        for word in line.split():
            try:
                numbers.append(float(word))
                correct = correct + 1
            except ValueError:
                print('{} is not a correct float number'.format(word))
                incorrect = incorrect + 1

    print('Loaded floats: {}'.format(correct))
    print('Incorrect values: {}'.format(incorrect))
    handle.close()
    numbers.sort()
    return numbers


def sMin(dataList):
    return dataList[0]


def sMax(dataList):
    return dataList[-1]


def sRange(dataList):
    return dataList[-1] - dataList[0]


def sMean(dataList):
    sum = 0
    i = 0
    for value in dataList:
        sum += value
        i += 1
    return sum / i


def sPercentile(dataList, k):
    if k <= 0 or k > 100:
        raise ValueError('ERROR: K <= OR k > 100')
    i = math.ceil(k * len(dataList) / 100)
    return dataList[i - 1];


def sMedian(dataList):
    return sPercentile(dataList, 50)


def sQuartiles(dataList):
    return (sPercentile(dataList, 25),
            sPercentile(dataList, 50),
            sPercentile(dataList, 75))


def sQuantiles(dataList, cutPoints):
    result = list()
    for c in cutPoints:
        result.append(sPercentile(dataList, c))


def sMode(dataList):
    currentVal = dataList[0]
    currentValoOcc = 1

    modeVal = 0
    modeValOcc = 0

    for val in dataList[1:]:
        if val == currentVal:
            currentValoOcc += 1
        else:
            if currentValoOcc > modeValOcc:
                modeVal = currentVal
                modeValOcc = currentValoOcc
            currentVal = val
            currentValoOcc = 1

    if currentValoOcc > modeValOcc:
        modeVal = currentVal
    return modeVal


def sModes(dataList):
    currentVal = dataList[0]
    currentValoOcc = 1

    modes = list()
    modesOcc = 1

    for val in dataList[1:]:
        if val == currentVal:
            currentValoOcc += 1
        else:
            if currentValoOcc > modesOcc:
                modes = [currentVal]
                modesOcc = currentValoOcc
            elif currentValoOcc == modesOcc:
                modes.append(currentVal)
            currentVal = val
            currentValoOcc = 1

    if currentValoOcc > modesOcc:
        modes = [currentVal]
    elif currentValoOcc == modesOcc:
        modes.append(currentVal)
    return modes


if __name__ == '__main__':
    try:
        dataList = [3, 6, 7, 8, 8, 9, 10, 10, 13, 13, 13, 15, 16, 16, 16, 20, 20, 20]
        print(sMode(dataList))
        print(sModes(dataList))
    except ValueError as error:
        print(error)
#    import sys
#    try:
#        data = getData(sys.argv[1])
#        if len(data) == 0:
#            print('Floats list is empty')
#        else:
#            print(data)
#            print('{} is min value'.format(sMin(data)))
#            print('{} is max value'.format(sMax(data)))
#            print('{} is range'.format(sRange(data)))
#            print('{} is mean'.format(sMean(data)))
#    except IOError as error:
#        print(error)
