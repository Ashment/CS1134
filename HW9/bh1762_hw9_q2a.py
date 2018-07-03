
#Best Worst Case
#Worse Case Θ(nlog(n))
def intersection_list(lst1, lst2):
	outLst = [];
	union = [e for e in lst1];
	union.extend(lst2);
	union.sort();
	pointer = 0;
	while pointer < len(union) - 1:
		if(union[pointer] == union[pointer+1]):
			outLst.append(union[pointer]);
		pointer += 1;
	return outLst;