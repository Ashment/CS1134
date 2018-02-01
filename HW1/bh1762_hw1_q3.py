import math

def SumOfSquares(n) :
	out=0;
	for i in range(n) :
		out += i**2
		
	return out;
	
def SumOfSqrComp(n) :
	return sum([i**2 for i in range(n)]);
	
def SumOfOddSqrC(n) :
	out=0;
	for i in range(n) :
		out += i**2 if i%2==1 else 0
		
	return out;
	
def SumOfOddSqrs(n) : 
	return sum([i**2 for i in range(n) if i%2==1]);
	
print (SumOfSquares(5))
print (SumOfSqrComp(5))
print (SumOfOddSqrC(5))
print (SumOfOddSqrs(5))
