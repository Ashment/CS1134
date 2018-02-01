
def FibGen (n) :
	fibList = [1];
	yield 1;

	for i in range(n-1) :
		if(len(fibList) == 1) :
			yield fibList[0];
			fibList.append(1)
		else :
			fibList.append(fibList[i] + fibList[i-1])
			yield fibList[i+1];


for i in FibGen(10) :
	print(i);