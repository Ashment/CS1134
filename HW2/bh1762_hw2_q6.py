

def two_sum(srt_lst, target) :
	lowerind = 0;
	upperind = len(srt_lst)-1;

	while lowerind != upperind :
		if(srt_lst[lowerind] + srt_lst[upperind] == target) :
			return [lowerind, upperind];
		elif (srt_lst[lowerind] + srt_lst[upperind] < target) :
			lowerind += 1;
		else :
			upperind -= 1;

	return None;


#srt_lst = [-2,7,11,15,20,21];
#print(two_sum(srt_lst, 36));