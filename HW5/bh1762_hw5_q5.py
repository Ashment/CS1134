
class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]

    def __repr__(self) :
        outArr = []
        for i in range(len(self.data)-1, -1, -1):
            outArr.append(str(self.data[i]));
        return '\n'.join(outArr);
        

def permutations(lst):
	tStack = Stack();
	print(tStack);

	##outArr = [[ ], [ ]]
	outArr = [[lst[len(lst)-1]]];

	for i in range(len(lst)-2,-1,-1):
	## i = int
#		print('# # # Now Creating Permutations for', str(lst[i]), '# # #');
#		print(outArr);

		#Empty outArr into tStack.
		while len(outArr) > 0 :
			tStack.push(outArr.pop());

		#Create Permutations around each member of tStack.
		while not tStack.is_empty():
			curVal = tStack.pop();
			##curval = array
#			print('# # Now Permutating around', str(curVal), '# #')


			for j in range(len(curVal)+1) :
				t = curVal.copy();
				t.insert(j, lst[i]);
				outArr.append(t);
#				print(outArr);
	
	return outArr;





























