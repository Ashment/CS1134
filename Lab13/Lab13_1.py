import ChainingHashTableMap

def most_frequent(lst):
	hTable = ChainingHashTableMap.ChainingHashTableMap();
	for e in lst:
		hTable[e] = 0;
	for e in lst:
		hTable[e] = hTable[e]+1;

	curMaxF = 0;
	for i in hTable:
		if(hTable[i] > curMaxF):
			curMaxF = hTable[i];
			curMaxE = i;

	return curMaxE;



def DEBUG():
	'''
	a = ChainingHashTableMap.ChainingHashTableMap();
	a[1] = 'a';
	a[2] = 'b';
	print(a[1]);
	print(a[2]);

	'''

	a = [1,2,3,4,9,9,2,3,9,1,9,9];
	print(most_frequent(a));


DEBUG();