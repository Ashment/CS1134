import DoublyLinkedList

def Prime_Factorization(intIn) :
	outList = DoublyLinkedList.DoublyLinkedList();
	rem = intIn;
	cur = 2;
	while cur < intIn//2 :
		if(rem%cur == 0) :
			outList.add_last(cur);
			rem = rem/cur
		else :
			cur += 1;
	if len(outList) == 1:
		outList.add_last(cur);

	return outList;

print(Prime_Factorization(82))