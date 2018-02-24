
def find_duplicates (inLst) :
	counterLst = [0 for i in range(len(inLst))];		#(n)
	# 	INDEX		 0  1  2  3  4  5      n-2
	#	LIST		[0, 0, 0, 0, 0, 0, ... ,0]
	# 	NUMBER		 1  2  3  4  5  6      n-1

	for num in inLst :									#(n)
#		print(num);
		counterLst[num] += 1;
#		print(counterLst[num-1]);

	outList = []
	for i in range(len(counterLst)):					#(n)
		if(counterLst[i] > 1) :
			outList.append(i);

	return outList;
#WORST CASE RUNNING TIME:
#	n + n + n
#	O(3n) > O(n)


'''
listT = [2,4,4,1,2];
print(FindDuplicates(listT));
'''