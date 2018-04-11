import DoublyLinkedList

class Integer :
	def __init__(self, numStr) :
		self.dataList = DoublyLinkedList.DoublyLinkedList();
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





















