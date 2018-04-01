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

    def __repr__(self) :
        outArr = []
        for i in range (self.front_ind, self.front_ind + self.number_of_elems) :
            pointer = i % len(self.data);
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

        self.number_of_elems += 1;
        self.data[pointer] = data;
        self.front_ind = pointer;


    def add_last(self, data) :
        super().enqueue(data);

    def del_first(self) :
        super().dequeue();

    def del_last(self) :
        if(self.is_empty()):
            raise Exception("Queue is empty")

        pointer = (self.front_ind + self.number_of_elems) % len(self.data);
        value = self.data[pointer];
        self.data[pointer] = None;

        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value


class BoostQueue(Queue) :

    def __init__(self):
        super().__init__();


    def boost(self, distance) :
        pointer = (self.front_ind + self.number_of_elems) % len(self.data) - 1;
        if(distance < self.number_of_elems):
            for i in range(distance) :
                self.data[pointer-1],self.data[pointer] = self.data[pointer],self.data[pointer-1]
                pointer -= 1;
        else :
            raise ValueError("Boost distance exceeds length of queue.")



















