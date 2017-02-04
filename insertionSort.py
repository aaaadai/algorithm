def insertionSort(sortingList):
	j = 1
	while (j<len(sortingList)):
		i = j - 1
		while (i >= 0):
			if (sortingList[j]>sortingList[i]):
				break
			i = i - 1
		insert(sortingList, j, i + 1)
		j = j + 1

def insert(insertingList, insertingIndex, insertedIndex):
	temp = insertingList[insertingIndex]
	j = insertingIndex - 1
	while(j>=insertedIndex):
		insertingList[j+1]=insertingList[j]
		j = j - 1
	insertingList[insertedIndex] = temp	

if __name__ == '__main__':
	exampleList = [5,4,6,2,1,8,9,8]
	insertionSort(exampleList)
	print(exampleList)