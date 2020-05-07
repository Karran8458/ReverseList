def reverse_list(arr):
	arr2=[ ]
	for x in range(len(arr)-1,0,-1):
		arr2.append(arr[x])
	arr2.append(arr[0])
	return arr2
		
