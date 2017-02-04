def selectionSort(sortingList):
	j = 0
	sortedList = []
	while (j<len(sortingList)):
		i = j + 1
		while (i<len(sortingList)):
			if (sortingList[i]<sortingList[j]):
				swap(sortingList,i,j)
			i = i + 1
		j = j + 1

def swap(swappingList, index1, index2):
	temp = swappingList[index1]
	swappingList[index1] = swappingList[index2]
	swappingList[index2] = temp
	
if __name__ == '__main__':
	exampleList = [5,4,6,2,1,8,9,8]
	selectionSort(exampleList)
	print(exampleList)