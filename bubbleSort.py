def bubbleSort(sortingList):
	sortedIndex = len(sortingList)
	while(sortedIndex > 1 ):
		j = 0
		while (j < sortedIndex - 1):
			if (sortingList[j]>sortingList[j+1]):
				swap(sortingList, j, j+1)
			j = j + 1
		sortedIndex = sortedIndex - 1

def swap(swappingList, index1, index2):
	temp = swappingList[index1]
	swappingList[index1] = swappingList[index2]
	swappingList[index2] = temp

if __name__ == '__main__':
	exampleList = [5,4,6,2,1,8,9,8,0]
	bubbleSort(exampleList)
	print(exampleList)