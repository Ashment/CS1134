
#################################################
##### D   I   S   C   L   A   I   M   E   R #####
#################################################
### Even though the homework instructions ask ###
### the homework questions be submitted as two ##
### separate files, the only way the autograder #
### is willing to accept an answer is if the  ###
### classes are pasted here. So here it is.   ###
### Piazza offered no productive answer,      ###
### stating that there is precedent for auto- ###
### grader giving all test case pass. Well,   ###
### here is the only way to get it to pass.   ###
### Thanks instructor for answering the       ###
### on Piazza!                                ###
#################################################


class Empty (Exception) :
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"



#################################################
##### D   I   S   C   L   A   I   M   E   R #####
#################################################
######### PLEASE READ DISCLAIMER AT TOP #########
### QUESTION RELEVANT CODE STARTS HERE. #########



class Integer :
	def __init__(self, numStr) :
		self.dataList = DoublyLinkedList();
		for num in numStr :
#			print("Adding Node to DataList |>", num)
			self.dataList.add_last(int(num));

	def __add__(self, other) :
#		print("NOW PERFOMRING ADDITION ON |> ", self, ' AND ', other);

		sCursor = self.dataList.trailer.prev
		oCursor = other.dataList.trailer.prev
		outStr = ''
		carry = 0

		while (sCursor is not self.dataList.header) or (oCursor is not other.dataList.header) :
			if(sCursor is self.dataList.header) :
#				print("sCursor ended.")
				res = oCursor.data + carry
				carry = 0
				if(res > 9) :
					res -= 10;
					carry = 1;
				outStr = str(res) + outStr;
				oCursor = oCursor.prev;
			elif(oCursor is other.dataList.header) :
#				print("oCursor ended.")
				res = sCursor.data + carry
				carry = 0
				if(res > 9) :
					res -= 10;
					carry = 1;
				outStr = str(res) + outStr;
				sCursor = sCursor.prev;
			else :
#				print("ADDITION |>", str(sCursor.data), "+", str(oCursor.data));
				res = sCursor.data + oCursor.data + carry;
				carry = 0
				if(res > 9) :
					res -= 10;
					carry = 1;
				outStr = str(res) + outStr;
				oCursor, sCursor = oCursor.prev, sCursor.prev;

		if(carry > 0):
			outStr = str(carry) + outStr;

		if(outStr == '0') :
			return Integer('0');

		leadZero = 0;
		while outStr[leadZero] == '0':
			leadZero += 1;

#		print(">>> RESULT STR :", outStr[leadZero:]);
		return Integer(outStr[leadZero:]);

	def __mul__(self, other) :
#		print("NOW PERFOMRING MULT ON |> ", self, ' AND ', other);

		sCursor = self.dataList.trailer.prev
		oCursor = other.dataList.trailer.prev
		mulResArr = [];
		carry = 0;
		for i in range(len(self.dataList)):
#			print('sCursor data :', sCursor.data);
			resStr = ''
			for j in range(len(other.dataList)):
#				print('oCursor data :', oCursor.data);
#				print('MULTIPLICATION STEP |>', sCursor.data, '*', oCursor.data);
				res = sCursor.data * oCursor.data;
				res += carry;
				carry, res = res//10, res%10
				oCursor = oCursor.prev
				resStr = str(res) + resStr
			mulResArr.append(Integer(str(int(resStr) * 10**(i))));
			sCursor = sCursor.prev
			oCursor = other.dataList.trailer.prev;

		if(carry > 0) :
			mulResArr.append(Integer(str(carry * 10**(len(self.dataList)))))
			

		out = Integer('0');
		for rslt in mulResArr :
			out = out + rslt;

#		print(">>>RESULT :", out);
		return out;



	def __repr__(self) :
		return ''.join([str(data) for data in self.dataList]);


def debug() :

	'''
	a = Integer("010000")
	b = Integer("00100")
	c = Integer("00000000000010")
	print(a+b+c);
	'''

	a = Integer("6");
	b = Integer("0");
	print(a*b);

#debug();





















