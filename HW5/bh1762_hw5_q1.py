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

        self.data[pointer] = data;
        self.front_ind = pointer;
        self.number_of_elems += 1;


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




def EvalPostfix(exp_str) :
    OpQueue = Deque();
    ArgQueue = Deque();
    Assign = False;

    for token in tokens(exp_str) :
        if(token in "+-/*") :
            OpQueue.enqueue(token);
        elif(token in "=") :
            dicName = ArgQueue.dequeue();
            Assign = True;
            print(dicName, Assign);
        else :
            ArgQueue.enqueue(token);

#    print(ArgQueue);
#    print()
#    print(OpQueue);
#    print()

    while not OpQueue.is_empty() :
        curOp = OpQueue.dequeue();
        arg1 = float(ArgQueue.dequeue());
        arg2 = float(ArgQueue.dequeue());
        if(curOp == '+'):
            ArgQueue.add_first(arg1+arg2);
        elif(curOp == '-'):
            ArgQueue.add_first(arg1-arg2);
        elif(curOp == '*'):
            ArgQueue.add_first(arg1*arg2);
        elif(curOp == '/'):
            ArgQueue.add_first(arg1/arg2);

    else :
        outArg = ArgQueue.dequeue();
        if Assign :
            return {dicName : outArg};
        else :
            return outArg;
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def tokens(exp_str):
    exp_str = exp_str.strip()
    n = len(exp_str)
    i = 0

    while(i < n):
        #skipping spaces
        while(exp_str[i] == ' '):
            i += 1
        if (exp_str[i] in "+-*/=" or exp_str[i].isalpha()):
            yield exp_str[i]
            i += 1

        else:
            digits_list = []
            while (i<n and exp_str[i].isdigit()):
                digits_list.append(exp_str[i])
                i += 1
            yield ''.join(digits_list)



def Main() :
    memDic = {};
    print('\nPostfix Arithmetic Interpreter Initiated...\nType "help" for help.');

    while True :
        userIn = input("-->")
        if(userIn == 'help'):
            help = '''
This is a postfix arithmetic interpreter. Supported operations are "+ - * /".
Arithmetic Syntax is as follows :
1 1 +
Variables can be a single alphabetic letter. Assignment syntax is as follows:
a = 3 2 -
            '''
            print(help);
        else :
            interpreted = EvalPostfix(userIn);
            if type(interpreted) == float or  type(interpreted) == int:
                print(interpreted);
            elif type(interpreted) == str :
                print(memDic[interpreted]);
            elif type(interpreted) == dict :
                memDic.update(interpreted);
                for key in interpreted :
                    print(key);


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


Main();







