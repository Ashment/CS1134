

'''
#EXAMPLE#
def remove_all(lst, val) :
	end = False;
	while(end == False) :
		try:
			lst.remove(val);
		except ValueError:
			end = true;

#Run Time: O(n^k) => O(n²)
'''

def swap(lst, ind1, ind2) :
	lst[ind1], lst[ind2] = lst[ind2], lst[ind1];


def remove_all(lstIn, val) :
	counter = 0;
	eOffset = 0;
	for i in range(len(lstIn)) :
		if(lstIn[i] == val) :
			if(i < len(lstIn)-(eOffset+1)) :
				swap(lstIn, i, len(lstIn)-(1+eOffset));
				eOffset += 1;
				counter += 1;

	for i in range (counter) :
		lstIn.pop();

	return lstIn;

'''
#Runtime : (n+k) => O(n)
'''


'''
lstT = [1,2,3,4,5,3,3,4,5,6];

print(lstT);
remove_all(lstT, 3);
print(lstT);
'''