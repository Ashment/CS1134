
#Best Worst Case
def intersection_list(lst1, lst2):
	outLst = [];
	for e in lst1:					# O(n)
		if e in lst2:				# > O(n)
			outLst.append(e);		#   > O(1)
	return outLst;


#Best Average Case
def intersection_list(lst1, lst2):
	sDict = {};
	outLst = [];
	for e in lst1:					# O(n)
		sDict[e] = 1;				# > O(1)
	for e in lst2:					# O(n)
		if(sDict[e] == 1):			# > O(1)
			outLst.append(e);

