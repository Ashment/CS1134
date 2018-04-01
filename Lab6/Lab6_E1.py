

def DecimalToBinary (inVal) :
	if(inVal > 1):
		rem = inVal;
		digits = 0;
		zeroes = 0;
		out = '1'

		while 2**digits < inVal :
			digits += 1;

		rem -= 2**(digits-1);
#		print('rem |> ' + str(rem))

		while 2**digits > rem :
			zeroes += 1;
			digits -= 1;
		zeroes -= 1;
		out += '0'*(zeroes-1)

		return out + DecimalToBinary(rem);
	else :
		return '1'


print(DecimalToBinary(200));