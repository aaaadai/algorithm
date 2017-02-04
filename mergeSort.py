def mergeSort(sortingList):
	mergeLength = 1
	while(mergeLength<len(sortingList)):#循环到merge array长度大于或等于array本身长度为止
		j = 0
		while(j+mergeLength<=len(sortingList)):
			index = j
			tempList1 = sortingList[j:j+mergeLength]
			if (j+2*mergeLength>len(sortingList)):
				tempList2 = sortingList[j+mergeLength:len(sortingList)]
			else:
				tempList2 = sortingList[j+mergeLength:j+2*mergeLength]
			while (index<j+2*mergeLength):
				# if 结构应该可以更简化
				if (tempList1 and tempList2):
					if (tempList1[0]<tempList2[0]):
						sortingList[index] = tempList1.pop(0)
					else:
						sortingList[index] = tempList2.pop(0)
				elif (tempList1):
					sortingList[index]=tempList1.pop(0)
				elif (tempList2):
					sortingList[index] = tempList2.pop(0)
				index = index + 1
			j = j + 2*mergeLength
		mergeLength = mergeLength * 2


if __name__ == '__main__':
	exampleList = [5,4,6,2,1,8,9,8,3]
	mergeSort(exampleList)
	print(exampleList)