

def ApproxSqrta (i) :
	out = 0.0;
	
	while out**2 < i :
		out += 0.01;

	return round(out-0.01, 2);


def ApproxSqrtb (i) :
	out = 0.0;

	#Find Uper Bound
	while out**2 < i :
		out +=1;
	#out -= 1;

	while out**2 > i :
		out -= 0.01;

	return round(out, 2);


print(ApproxSqrta(123456789));
print(ApproxSqrtb(123456789));
