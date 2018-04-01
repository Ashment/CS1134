

def appearances (s, low, high, dic=None) :
	if(dic == None) :
		dic = {};

	if(low > high) :
		return dic;
	else :
		if(s[low] in dic) :
			dic.update({s[low]:dic[s[low]]+1});
			return appearances(s, low+1, high, dic);
		else :
			dic.update({s[low]:1});
			return appearances(s, low+1, high, dic);