

def ListGen (inList) :
	return [inList[i] for i in range(len(inList)) if(inList[i]%2==0 and i%2 == 0)];

lst = [2,3,5,6,8,8];
print(ListGen(lst));