

def FindLstMax (lst) :
	if(len(lst) == 1):
		print("FOUND");
		return lst[0];

	if(lst[0] > lst[len(lst)-1]) :
		return FindLstMax(lst[:len(lst)-1]);
	else :
		return FindLstMax(lst[1:]);

lstT = [1,2,3,4,5,100,3,2];
c = FindLstMax(lstT);
print(c);
