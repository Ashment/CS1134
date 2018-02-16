import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:

    ######## ATTRIBUTES #######
    ##          data         ##
    ##        capacity       ##
    ##            n          ##
    ###########################

    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1


    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size


    def __len__(self):
        return self.n


    def __getitem__(self, ind):
        #Get Slice Index Type
        if(isinstance(ind, int)) :
            if(ind >= 0 and ind <= self.n -1) :
                return self.data[ind];
            elif(ind < 0 and ind >= -(self.n)-1) :
                return self.data[self.n+ind];
            else :
                raise IndexError("invalid index");
        elif(isinstance(ind, slice)) :
            #Set Slice Index Defaults
            start = 0 if ind.start==None else ind.start;
            stop = len(self)-1 if ind.stop==None else ind.stop;
            step = 1 if ind.step==None else ind.step;

            if(0 <= start < len(self) and start <= start < len(self)):
                outList = MyList();
                for i in range(start, stop//step+1) :
                    if(i%step == 0):
                        outList.append(self[i*step]);

                return outList;
            else :
                raise IndexError("invalid index range")
        else :
            raise TypeError("Invalid Index Type");


    def __setitem__(self, ind, val):
        if (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        self.data[ind] = val


    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]


    def __repr__(self):
        out = '['
        for i in range(self.n):
            out += str(self.data[i]);
            out += ', ';
        out = out[:-2];
        out += ']';
        return out;


    def __add__(self, other):
        outList = MyList();
        for i in self:
            outList.append(i);
        for i in other:
            outList.append(i);
        return outList;


    def __iadd__(self, other):
        for i in other:
            self.append(i);
        return self;


    def __mul__(self, other):
        outList = MyList();
        for m in range(other) :
            for i in self:
                outList.append(i);
        return outList;


    def __rmul__(self, other):
        outList = MyList();
        for m in range(other) :
            for i in self:
                outList.append(i);
        return outList;


    def extend(self, iterable_collection):
        for elem in iterable_collection:
            self.append(elem)


# -------------------------------------------------------#


#TESTIN PARAMETERS
mL = MyList();
mL.resize(5);
mL.append(10);
mL.append(20);
mL.append(30);
mL.append(40);
mL.append(50);
mmL = MyList();
mmL.append(100);
mmL.append(200);



'''
#Slice Testing
print(mL[0:3]);
print(mL[0:4]);
print(mL[0:4:2])
'''

'''
#Mul Testing
print(mL * 2);
print(2 * mL);
'''

'''
#Indeces Testing
print(mL[4]);
print(mL[3]);
print(mL[-1]);
print(mL[-2]);
print(mL[-4]);
print(mL[-5]);
'''

'''
#Add Testing
print(mL + mmL);
print(mmL + mL);
'''















