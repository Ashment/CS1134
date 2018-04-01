import DoublyLinkedList


def ReverseNodeData(lnklst) :
	fPointer=lnklst.header.next
	bPointer=lnklst.trailer.prev

	while(bPointer.next is not fPointer) and (bPointer is not fPointer) :
		fPointer.data, bPointer.data = bPointer.data, fPointer.data;
		fPointer = fPointer.next
		bPointer = bPointer.prev

	return lnklst;

def ReverseNodePos(lnklst) :
	#Initalize pointers
	fPointer=lnklst.header.next
	bPointer=lnklst.trailer
	
	for i in range(len(lnklst)) :
		tPointer = fPointer.next;
		fPointer.next = bPointer;
		bPointer.prev = fPointer;
		fPointer, bPointer = tPointer, fPointer;

	lnklst.header.next = bPointer;
	bPointer.prev = lnklst.header;




a = DoublyLinkedList.DoublyLinkedList();
a.add_last(1);
a.add_last(2);
a.add_last(3);
a.add_last(4);
print(a);
ReverseNodePos(a);
print(a);

