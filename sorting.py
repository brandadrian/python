class Sorting():
    def bubbleSort(self, inputList):
        length = len(inputList)
        temp = 0
        for i in range(0, length):
            for j in range(0, length - i - 1):
                if (inputList[j] > inputList[j + 1]):
                    temp = inputList[j]
                    inputList[j] = inputList[j + 1]
                    inputList[j + 1] = temp
        return inputList       
        
test = Sorting()
listToSort = [5, 2, 3, 1, 6]
print(test.bubbleSort(listToSort))
