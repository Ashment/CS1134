
def NestedSums(inval) :

	out = 0;

	if(isinstance(inval, list)):
		for val in inval:
			out += NestedSums(val);
		return out;

	else:
		return inval


lstT = [1,2,[3,4,5],[6,[7,8,9]]];

print(NestedSums(lstT));
