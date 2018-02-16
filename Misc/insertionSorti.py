
def InsertionSort(l) :
	for i in range(1, len(l)) :
		print ('- - - - - - - - - -');
		print(l);
		curVal = l[i];
		ind = i;

		while ind > 0 and l[ind-1] > curVal :
			l[ind] = l[ind-1];
			ind -= 1;
			l[ind] = curVal;

Z = [4,3,2,5,1];
InsertionSort(Z);
print(Z);
