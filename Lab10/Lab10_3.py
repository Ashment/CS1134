import DoublyLinkedList

def FlattenLinkedListRec(lst) :
	out = DoublyLinkedList.DoublyLinkedList();
	cursor = lst.first_node();
	while cursor is not lst.trailer:
		if(type(cursor.data) == int):
			out.add_last(cursor.data);
		else:
			nestList = FlattenLinkedList(cursor.data);
			nestCursor = nestList.first_node();
			while nestCursor is not nestList.trailer:
				out.add_last(nestCursor.data);
				nestCursor = nestCursor.next;
		cursor = cursor.next;
	return out


def FlattenLinkedListIter(lst) :
	t = DoublyLinkedList.DoublyLinkedList();
	tC = lst.first_node();

	while tC is not lst.trailer:
		t.add_last(tC.data);
		tC = tC.next;

	lstStack = DoublyLinkedList.DoublyLinkedList();
	out = DoublyLinkedList.DoublyLinkedList();
	lstStack.add_last(t);


	while not lstStack.is_empty():
		t = lstStack.first_node().data;
		lstStack.delete_first();
		print(" > > Now Iterating:",t);
		fData = t.first_node().data;
		t.delete_first();


		if(len(t) > 0):
			lstStack.add_first(t);
			print("Returning to lstStack:", t)

			
		if(type(fData) == int):
			out.add_last(fData);
			print("Adding to out:", fData);
		else:
			lstStack.add_first(fData);
			print("Adding to lstStack:", fData);

	return out;




a = DoublyLinkedList.DoublyLinkedList();
b = DoublyLinkedList.DoublyLinkedList();

a.add_last(1);
a.add_last(2);
a.add_last(3);
b.add_last(4);
b.add_last(5);
a.add_last(b);
a.add_last(6);

print(a);
print(FlattenLinkedListIter(a));
