import random

def quickSort(sortingList):
	quickSort2(sortingList,0,len(sortingList)-1)

def quickSort2(sortingList,start,end):
	if end - start < 20 and start < end:
		sortingList[start:end+1] = sorted(sortingList[start:end+1])
	elif start < end:
		pIndex = partitioning(sortingList,start,end)
		quickSort2(sortingList,start,pIndex)
		quickSort2(sortingList,pIndex+1,end)

def adjustPivot(currentList):
	mid = (len(currentList)-1)//2
	s = sorted([currentList[0],currentList[mid],currentList[-1]])
	if s[1] == currentList[0]:
		currentList[0],currentList[-1] = currentList[-1],currentList[0]
		return
	elif s[1] == currentList[mid]:
		currentList[mid],currentList[-1] = currentList[-1],currentList[mid]
		return
	return

def partitioning(partioningList,start,end):
	adjustPivot(partioningList[start:end+1])
	pIndex = 0
	for i in range(start,end+1):
		if partioningList[i] < partioningList[-1]:
			partioningList[i],partioningList[pIndex] = partioningList[pIndex],partioningList[i]
			pIndex += 1
	partioningList[-1],partioningList[pIndex] = partioningList[pIndex],partioningList[-1]
	return pIndex


if __name__ == '__main__':
	#exampleList = [5,4,6,2,1,8,9,8,3]
	exampleList = [random.randint(0, 1000000) for a in range(0, 50)]
	quickSort(exampleList)
	print(exampleList)