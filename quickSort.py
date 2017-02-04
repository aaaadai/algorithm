def quickSort(sortingList):
#	while():
#		wall = partioning(sortingList)
#		if (wall == 0 or wall == len(sortingList)-1):
#			break
#		else:
#			subwall1 = 

def partioning(partioningList):
	wall = 0
	while (1):
		j = wall
		while(j<len(partioningList)-1):
			if(partioningList[j]<partioningList[-1]):
				swap(partioningList, wall, j)
				break;
			j = j + 1
		if(j == len(partioningList)-1):
			swap(partioningList, wall, j)
			break;
		wall = wall + 1
	return wall

def swap(swappingList, index1, index2):
	temp = swappingList[index1]
	swappingList[index1] = swappingList[index2]
	swappingList[index2] = temp

if __name__ == '__main__':
	exampleList = [5,4,6,2,1,8,9,8,3]
	print(partioning(exampleList))
	print(exampleList)