class Empty (Exception) :
    pass


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

    def __repr__(self):
        outArr = []
        for i in range(0, len(self.data), 1):
            outArr.append(self.data[i]);
        return str(outArr);


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Queue :

	def __init__(self):
		self.inStack = Stack();
		self.outStack = Stack();

	def is_empty(self):
		return (self.inStack.is_empty() and self.outStack.is_empty()); 

	def enqueue(self, elem):
		while len(self.outStack) > 0:
			self.inStack.push(self.outStack.pop());
		self.inStack.push(elem);

	def dequeue(self):
		if(self.is_empty()):
			raise Empty('Queue is Empty...')
		while len(self.inStack) > 0:
			self.outStack.push(self.inStack.pop());
		return self.outStack.pop();

	def __repr__(self):
		if(self.inStack.is_empty()):
			outArr = [];
			for i in range(len(self.outStack)-1, -1, -1):
				outArr.append(self.outStack.data[i]);
			return str(outArr);
		else:
			return str(self.inStack);

	def first(self):
		if (self.is_empty()):
			raise Exception("Queue is empty");
		else :
			if(self.inStack.is_empty()):
				return self.outStack.data[-1];
			else:
				return self.inStack.data[0];



'''
a = Queue();
a.dequeue();
a.enqueue(1);
a.enqueue(2);
a.enqueue(3);
a.enqueue(4);
a.enqueue(5);
a.enqueue(6);
print(str(a.inStack), ' | ', str(a.outStack));
#print(a);
a.dequeue();
a.dequeue();
print(a);
#a.enqueue(7);
#print(a.first());
a.dequeue();
a.dequeue();
a.dequeue();
a.dequeue();
'''













