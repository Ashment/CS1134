class Queue:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = [None] * Queue.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0

    def __repr__(self):
        outArr = []
        for i in range (self.front_ind, self.front_ind + self.number_of_elems) :
            pointer = i % (len(self.data));
            outArr.append(self.data[pointer]);
        return str(outArr);


class Deque (Queue) :

    def __init__(self):
        super().__init__();


    def first(self):
        return self.data[self.front_ind];

    def last(self):
        pointer = (self.front_ind + self.number_of_elems) % len(self.data) - 1;
        return self.data[pointer];

    def add_first(self, data) :
        #Resize if necessary
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))

        if(self.front_ind == 0) :
            pointer = len(self.data) - 1
        else :
            pointer = self.front_ind - 1

        self.data[pointer] = data;
        self.front_ind = pointer;
        self.number_of_elems += 1;

    def add_last(self, data):
        super().enqueue(data);

    def del_first(self):
        super().dequeue();

    def del_last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")

        pointer = (self.front_ind + self.number_of_elems) % len(self.data)-1;
        value = self.data[pointer];
        self.data[pointer] = None;

        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

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


class MidStack:

    def __init__(self):
        self.fHalf = Stack();
        self.sHalf = Deque();

    def is_empty(self):
        return (self.fHalf.is_empty() and self.sHalf.is_empty());

    def __len__(self):
        return (len(self.fHalf) + len(self.sHalf));

    def push(self, elem):
        self.sHalf.enqueue(elem);
        self.__Rebalance();

    def top(self):
        if(self.sHalf.is_empty()):
            return self.fHalf.top();
        else:
            return self.sHalf.last();

    def __Rebalance(self):
        if(len(self.sHalf) > len(self.fHalf)):
            self.fHalf.push(self.sHalf.dequeue());
        elif(len(self.fHalf) > len(self.sHalf) + 1):
            self.sHalf.add_first(self.fHalf.pop());

    def pop(self):
        if(self.sHalf.is_empty()):
            return self.fHalf.pop();
        else:
            val = self.sHalf.del_last()
            self.__Rebalance();
            return val;

    def mid_push(self, elem):
        self.sHalf.add_first(elem);
        self.__Rebalance();

    def __repr__(self):
        return str(self.fHalf) + ' | ' + str(self.sHalf);




'''
a = MidStack();
a.push(1);
a.push(2);
a.push(3);
a.push(4);
a.push(5);

#a.mid_push(100);
print(a);
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())


print();
print();
t = Deque();
t.enqueue(1);
t.enqueue(2);
t.enqueue(3);
t.enqueue(4);
print(t);
print(t.del_last());
print(t);
print(t.del_last());
print(t.del_last());
print(t.del_last());
print(t);
'''
















