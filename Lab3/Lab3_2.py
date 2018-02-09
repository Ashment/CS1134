

def SrtLstIntersection (in1, in2) :
	ind1 = 0;
	ind2 = 0;
	outLst = [];

	#Compare two inds
	while ind1 < (len(in1)) and ind2 < (len(in2)):
		#Add to Output if equal
		if (in1[ind1] == in2[ind2]) :
			outLst.append(in1[ind1]);
			ind1 += 1;
		#Move indeces is not equal.
		elif(in1[ind1] > in2[ind2]) :
			ind2 += 1;
		else :
			ind1 += 1;

	return outLst;
#Function Time Complexity : O(n)


lstT = [1,5,10,20];
lstY = [2,4,8,10,16,20];
print(SrtLstIntersection(lstT,lstY));
