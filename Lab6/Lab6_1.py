

def PowerOfTwo(num) :
	for i in range(1, num+1) :
		yield 2**i;



for i in PowerOfTwo(5):
	print(i);