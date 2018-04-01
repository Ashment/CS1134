

def count_lowercase(s, low, high, cur=0) :
	if(low > high) :
		return cur;
	else :
		if(s[low].islower()) :
			return count_lowercase(s,low+1,high,cur+1);
		else :
			return count_lowercase(s,low+1,high,cur);

def is_number_of_lowercase_even(s, low, high) :
	if(count_lowercase(s,low,high)%2 == 0) :
		count_lowercase(s,low,high)
		return True;
	else :
		count_lowercase(s,low,high)
		return False;