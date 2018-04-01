import DoublyLinkedList

class LinkedStack (DoublyLinkedList.DoublyLinkedList) :
	def __init__(self) :
		super().__init__();

	def push(self, e) :
		super().add_last(e);

	def pop(self) :
		return super().delete_last();

	def top(self) :
		return super().last_node().data;



a = LinkedStack();
a.push(1);
a.push(2);
a.push(3);
print(a);
a.pop();
a.pop();
print(a);
a.push(20);
a.push(30);
print(a);
print(a.top());