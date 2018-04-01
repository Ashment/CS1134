import ArrayStack


def ConvertInfixToPostfix(exp_str) :
	opsStack = ArrayStack.Stack();
	outLst = [];

	for token in tokens(exp_str) :
		if (token.isdigit()): #token is a numeral
			outLst.append(token)
		elif (token in '(+-*/'):
			print('Pushing to opsStack |>', token)
			opsStack.push(token)
		else :
			outLst.append(opsStack.pop());
			opsStack.pop();

	return ' '.join(outLst);

            


def tokens(exp_str):
    exp_str = exp_str.strip()
    n = len(exp_str)
    i = 0

    while(i < n):
        #skipping spaces
        while(exp_str[i] == ' '):
            i += 1
        if (exp_str[i] in "()<>+-*/&|"):
            yield exp_str[i]
            i += 1
        else:
            digits_list = []
            while (i<n and exp_str[i].isdigit()):
                digits_list.append(exp_str[i])
                i += 1
            yield ''.join(digits_list)



testExp = '(2 + ((3*4) - 5))'
print(ConvertInfixToPostfix(testExp));
