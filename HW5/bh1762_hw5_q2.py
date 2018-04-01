class Empty (Exception) :
    pass


class MaxStack:
    def __init__(self):
        self.__data = [];

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, elem):
        if (len(self) == 0) :
            self.__data.append((elem, elem));

        else :
            curMax = self.__data[-1][1]

            if (elem > curMax) :
                self.__data.append((elem, elem));
            else :
                self.__data.append((elem, curMax));

    def pop(self):
        if (self.is_empty() == True):
            raise Empty("Stack is empty")
        topTup = self.__data.pop()
        return  topTup[0];

    def top(self):
        if (self.is_empty() == True):
            raise Empty("Stack is empty")
        return self.__data[-1][0]

    def __repr__(self) :
        outArr = []
        for i in range(len(self.__data)-1, -1, -1):
            outArr.append(str(self.__data[i][0]));
        return '\n'.join(outArr);

    def max(self) :
        if (self.is_empty() == True):
            raise Empty("Stack is empty")
        return self.__data[-1][1];



'''
a = MaxStack();
print(a.max());
a.push(1);
print(a)
a.push(2);
a.push(100);
a.push(3);
print(a);
print();
print(a.max());
print();
a.pop();
a.pop();
print(a);
print();
print(a.max());
'''





