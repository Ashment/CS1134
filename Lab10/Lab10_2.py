import DoublyLinkedList

class BoostQueue :
	def __init__(self):
		self.queue = DoublyLinkedList.DoublyLinkedList();

	def __len__(self):
		return len(self.queue);

	def is_empty(self):
		return self.queue.is_empty();

	def enqueue(self, e):
		self.queue.add_last(e);

	def dequeue(self):
		out = self.queue.first_node().data;
		self.queue.delete_first();
		return out;

	def first(self):
		return self.queue.first_node().data;

	def boost(self, k):
		if(k > len(self)-1) :
			raise ValueError('Boost distance exceeds length');
		e = self.queue.delete_node(self.queue.last_node());
		cursor = self.queue.last_node();
		for i in range(k):
			cursor = cursor.prev;
		self.queue.add_after(cursor, e);

	def __repr__(self):
		return str(self.queue);



a = BoostQueue()
a.enqueue(0);
a.enqueue(1);
a.enqueue(2);
a.enqueue(3);
print(a);
a.dequeue();
print(a);
a.boost(3);
print(a);
