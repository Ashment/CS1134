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

    def __repr__(self) :
        outArr = []
        for i in range(len(self.data)-1, -1, -1):
            outArr.append(str(self.data[i]));
        return '\n'.join(outArr);
