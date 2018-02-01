

def ListGen (inList) :
	return [inList[i] for i in range(len(inList)) if(inList[i]%2==0 and i%2 == 0)];