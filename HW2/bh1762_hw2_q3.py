
def factors (n) :
	for i in range (1, int(pow(n, 0.5))+1) :
		if(n%i == 0) :
			yield i;
			if(n/i != int(pow(n, 0.5))) :
				yield int(n/i);

#for ea in factors(100) :
#	print (ea);