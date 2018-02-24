

def ProductEvens(lst) :
	if(len(lst)==1) :
		return lst[0];

	for i in range(len(lst)) :
		if(lst[i]%2==0 and lst[i]<=len(lst)):
			return lst[i] * ProductEvens(lst[i+1:]);
	return 1;


lstT = [1,2,3,4,5,100,3,2];
print(ProductEvens(lstT));