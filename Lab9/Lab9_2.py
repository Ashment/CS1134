import DoublyLinkedList

class LeakyStack (DoublyLinkedList.DoublyLinkedList) :
	def __init__(self, cap) :
		super().__init__();
		self.cap = cap;

	def push(self, e) :
		super().add_last(e);
		if(len(self) > self.cap) :
			self.header.next = self.header.next.next;

	def pop(self) :
		return super().delete_last();

	def top(self) :
		return super().last_node().data;



a = LeakyStack(5);

a.push(1);
a.push(2);
a.push(3);
a.push(4);
a.push(5);
a.push(6);
print(a);
a.pop();
a.pop();
print(a);
