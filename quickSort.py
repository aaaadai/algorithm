import random

def quick_sort(A):
	quick_sort2(A,0,len(A)-1)

def quick_sort2(A,low,hi):
	if hi - low < 20 and low < hi:
		quick_selection(A,low,hi)
	elif low < hi:
		p = partition(A,low,hi)
		quick_sort2(A,low,p-1)
		quick_sort2(A,p+1,hi)

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

def partition(partioningList,start,end):
	adjustPivot(partioningList[start:end+1])
	pIndex = start
	for i in range(start,end+1):
		if partioningList[i] < partioningList[-1]:
			partioningList[i],partioningList[pIndex] = partioningList[pIndex],partioningList[i]
			pIndex += 1
	partioningList[-1],partioningList[pIndex] = partioningList[pIndex],partioningList[-1]
	return pIndex

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]


if __name__ == '__main__':
	#exampleList = [5,4,6,2,1,8,9,8,3]
	exampleList = [random.randint(0, 1000000) for a in range(0, 50)]
	quick_sort(exampleList)
	print(exampleList)