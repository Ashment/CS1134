import ctypes

def make_array(n):
	return (n * ctypes.py_object)()

class MyString :

	######## ATTRIBUTES #######
	##          data         ##
	##        capacity       ##
	##           n           ##
	###########################

	def __init__ (self, inString) : 
		self.data = make_array(len(inString));
		self.n = self.capacity = len(inString);
		for i in range(len(inString)) :
			self.data[i] = inString[i];

	def __len__(self) :
		return self.n;

	def __iter__(self) :
		for i in range(self.n):
			yield self.data[i];

	def __repr__(self) :
		out = '';
		for i in range(self.n):
			out += self.data[i];
		return out

	def __add__(self, other) :
		cString = str(self) + str(other);
		return MyString(cString);

	def __radd__(self, other) :
		cString = str(other) + str(self);
		return MyString(cString);

	def __iadd__(self, other) :
		return MyString((str(self) + str(other)));

	def upper(self) :
		return MyString(str(self).upper());


s1 = MyString('abc')
s2 = MyString('def')
print(s1, len(s1));
print(s2, len(s2));
print(s1+s2);
print(s2+s1);
print(s1.upper());
s1 += s2
print(s1);