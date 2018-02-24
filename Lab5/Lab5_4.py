

def RecursiveBinarySearch(lst, target, indL=0, indH=None) :
	if(indH == None) :
		indH = len(lst)-1;
	midInd = (indL+indH)//2;
	print('midind : ', str(midInd));

	if(lst[midInd] == target) :
		return midInd;
	elif (lst[midInd] < target) :
		return RecursiveBinarySearch(lst, target, midInd, indH);
	else :
		return RecursiveBinarySearch(lst, target, indL, midInd);


lstT = [1,2,3,4,5];
lstR = [2,3,4,5,6,7];

print(RecursiveBinarySearch(lstT, 3));
print(RecursiveBinarySearch(lstR, 3));
print(RecursiveBinarySearch(lstR, 4));
print(RecursiveBinarySearch(lstR, 5));