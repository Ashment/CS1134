import random

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def disconnect(self):
        self.data = None
        self.prev = None
        self.next = None

    def unlinkSelf(self):
        succ = self.next;
        pred = self.prev;
        pred.next = succ;
        succ.prev = pred;
        self.disconnect();


class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

        self.keyHeader = Node();
        self.keyTrailer = Node();
        self.curCursor = self.keyHeader;

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        keyNode = Node();
        keyNode.data = key;
        keyNode.prev = self.curCursor;
        self.curCursor.next = keyNode;
        keyNode.next = self.keyTrailer;
        self.curCursor = self.curCursor.next;
        pVal = (keyNode, value);

        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap()
        old_size = len(self.table[i])
        self.table[i][key] = pVal;
        new_size = len(self.table[i])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        delNode = self[key][1];
        delNode.unlinkSelf();

        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[i] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        iCursor = self.keyHeader.next;
        while iCursor is not self.keyTrailer:
            cData = iCursor.data;
            iCursor = iCursor.next;
            yield cData;


    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value



class UnsortedArrayMap:

    class Item:
        def __init__(self, key, keyNode, value=None):
            self.key = key
            self.value = [value, keyNode];


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value[0];
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value[0] = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value[1], value[0]))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

