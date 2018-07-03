
#Best Average Case                  #Θ(n)
def intersection_list(lst1, lst2):
	print("Start Function")
	print(lst1, lst2);
	sDict = {};
	outLst = [];
	for e in lst1:					# O(n)
		print("Setting Item in Dict:", e);
		sDict[e] = 1;				# > O(1)
	for e in lst2:					# O(n)
		try:
			if(sDict[e] == 1):			# > O(1)
				print("Intersection Found:", e);
				outLst.append(e);
		except Exception:
			pass;

	return outLst;