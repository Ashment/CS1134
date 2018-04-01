

def SortPivotFirst(lst) :
	i = 0
	top = len(lst) - 1;
	while i < len(lst)-1 and i <= top :
#		print (lst, i);
		if(lst[i] > lst[i+1]) :
			lst[i], lst[i+1] = lst[i+1],lst[i];
			i += 1;
		else :
			lst[i+1], lst[top] = lst[top],lst[i+1];
			top -= 1;
	return lst


lstT = [54,26,93,17,77,31,44,55,20];

print(lstT);
SortPivotFirst(lstT);
print(lstT);

