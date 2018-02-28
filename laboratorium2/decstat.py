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


if __name__ == '__main__':
    import sys

    try:
        data = getData(sys.argv[1])
        if len(data) == 0:
            print('Floats list is empty')
        else:
            print(data)
            print('{} is min value'.format(sMin(data)))
            print('{} is max value'.format(sMax(data)))
            print('{} is range'.format(sRange(data)))
            print('{} is mean'.format(sMean(data)))
    except IOError as error:
        print(error)



