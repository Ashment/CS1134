import ArrayQueue

def SumNestedList (lst) :
	lstQ = ArrayQueue.Queue();
	lstQ.enqueue(lst);
	out = 0;

	while len(lstQ) > 0 :
		val = lstQ.dequeue();
		#print(val)

		for i in val : 
			if type(i) == list:
				lstQ.enqueue(i);

			elif type(i) == int:
				out += i;

			else :
				raise ValueError("Invalid type in list.")

	return out;

a = [[1, 2], [3, [[4], 5]], 6];

print(SumNestedList(a));