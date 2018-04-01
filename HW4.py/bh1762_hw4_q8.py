

def flat_list(lst, low, high) :
	out = [];
	for i in range(low, high+1) :
		if(isinstance(lst[i],list)) :
			out.extend(flat_list(lst[i],0,len(lst[i])-1));
		else :
			out.append(lst[i]);
	return out;


#lstT = [1,2,3,[2,3,4],5,6,7,8];
#lstR = [[[1]],2,3];
#print(flat_list(lstR,0,2));