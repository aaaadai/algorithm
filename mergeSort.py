import random

def mergeSort(sortingList):
	mergeSort2(sortingList,0,len(sortingList)-1)

def mergeSort2(sortingList, first, last):
	if last - first < 20 and first < last:
		sortingList[first:last+1] = sorted(sortingList[first:last+1])
	elif first < last:
		middle = (first + last)//2
		mergeSort2(sortingList,first,middle)
		mergeSort2(sortingList,middle+1,last)
		merge(sortingList,first,middle,last)

def merge(mergingList,first,middle,last):
	L = mergingList[first:middle+1]
	R = mergingList[middle+1:last+1]
	for j in range(first,last+1):
		if (L and R):
			if L[0] > R[0]:
				mergingList[j] = R.pop(0)
			else:
				mergingList[j] = L.pop(0)
		elif(L):
			mergingList[j] = L.pop(0)
		elif(R):
			mergingList[j] = R.pop(0)

if __name__ == '__main__':
	exampleList = [random.randint(0, 1000000) for a in range(0, 1000)]
	mergeSort(exampleList)
	print(exampleList)