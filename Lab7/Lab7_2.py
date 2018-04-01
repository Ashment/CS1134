
import ArrayStack


def EvalPostfixBool(exp_str) :
	CompStack = ArrayStack.Stack();
	ArgStack = ArrayStack.Stack();
	LogicStack = ArrayStack.Stack();

	for token in tokens(exp_str) :
		if(token in "<>") :
			CompStack.push(token);
		elif(token in "&|") :
			LogicStack.push(token);
		else :
			ArgStack.push(token);

	print(ArgStack);
	print()
	print(CompStack);
	print()
	print(LogicStack);
	print()

	if not LogicStack.is_empty() :
		logic = LogicStack.pop();
		comp1 = CompStack.pop();
		comp2 = CompStack.pop();
		arg22 = int(ArgStack.pop());
		arg21 = int(ArgStack.pop());
		arg12 = int(ArgStack.pop());
		arg11 = int(ArgStack.pop());
		if(comp1 == '>') :
			res1 = arg11 > arg12;
		elif(comp1 == '<') :
			res1 = arg11 < arg12;
		else :
			raise Exception("Unknown comparator in expression one")
		if(comp2 == '>') :
			res2 = arg21 > arg22;
		elif(comp2 == '<') :
			res2 = arg21 < arg22;
		else :
			raise Exception("Unknown comparator in expression two")

#		print(res1, res2)

		if(logic == '&') :
			if(res1 and res2) :
				return True
			else :
				return False
		elif(logic == '|') :
			if(res1 or res2) :
				return True
			else :
				return False
	else :
		raise Exception("Unknown boolean or boolean missing")
			



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



testExp = '2 5 > 8 3 > &'
print(EvalPostfixBool(testExp));