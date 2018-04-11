import DoublyLinkedList

class LinkedQueue :

	def __init__ (self) :
		self.queue = DoublyLinkedList.DoublyLinkedList();

	def is_empty (self) :
		return self.queue.is_empty();

	def enqueue(self, e) :
		self.queue.add_last(e)

	def dequeue(self) :
		if(self.is_empty()) :
			raise Exception('Nothing to dequeue.');

		val = self.queue.header.next.data
		self.queue.delete_node(self.queue.first_node())
		return val;

	def first (self) :
		return self.queue.first_node().data

	def __len__ (self) :
		return len(self.queue);

	def __repr__ (self) :
		return "[" + ", ".join([str(item) for item in self.queue]) + "]"



def debug() :
	a = LinkedQueue();
	a.enqueue(1);
	a.enqueue(2);
	a.enqueue(3);
	print(a)
	print(a.first())
	print(a.dequeue());
	print(a.dequeue());
	print(a.dequeue());
	print(a);

#debug();











