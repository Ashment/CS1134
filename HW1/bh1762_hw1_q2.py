def shift (inList, k, dir='left') :
	if dir=='left' :
		for rec in range(k) :
			temp = inList[0];
#			print ("Temp : " + str(temp));

			for ind in range(len(inList)-1) :
				inList[ind] = inList[ind+1];
#				print(inList)

			inList[len(inList)-1] = temp;

	else :
		for rec in range(k) :
			temp = inList[len(inList)-1];
#			print ("Temp : " + str(temp));

			for ind in range(len(inList)-1, 0, -1) :
				inList[ind] = inList[ind-1];
#				print(inList)

			inList[0] = temp;


#lstT = [1,2,3,4,5];
#print(lstT);
#Shift(lstT,2);
#print();
#print(lstT);
#Shift(lstT,2,'right');
#print();
#print(lstT);
