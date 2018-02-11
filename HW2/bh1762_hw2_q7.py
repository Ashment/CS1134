
def findChange(inLst) :
	lowerind = 0;
	upperind = len(inLst)-1;

	curind = 0;
	#while lowerind != upperind :
	while upperind - lowerind != 1 :
		curind = (lowerind+upperind)//2;

		#################################
		# print('lowerind', lowerind);	#
		# print('upperind', upperind);	#
		# print('curind', curind);		#
		#################################

		if(inLst[curind] == 1) :
			upperind = curind
			#print('upperind moved')
		elif(inLst[curind] == 0):
			lowerind = curind
			#print('lowerind moved')

		print();

	return upperind;


#lst = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1];

#print(findChange (lst));