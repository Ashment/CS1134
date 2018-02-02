

def EndZeroSort(inList) :
	offset = 0;
	for i in range(len(inList)) :						#ϴ(n)
		if(inList[i-offset]) == 0 :
			inList.append(inList.pop(i-offset));		#ϴ(k) + ϴ(1)
			offset += 1;								#K is length of inList
		print(i);
	return inList;

														#Total: ϴ(n)

print(EndZeroSort([1,0,0,2,3,4,0,5]));
