
def split_parity(inArr) :
	offset = 0;
	for i in range(len(inArr)) :
		if(inArr[i-offset]%2 == 0) :
			print(inArr[i-offset]);
			inArr.append(inArr.pop(i-offset));
			offset += 1;
		else :
			print(inArr[i-offset]);
	return inArr;


#t = [1,2,3,4];
#print(split_parity(t));
#print(t);