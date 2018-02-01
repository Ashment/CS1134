import math

class Vector :

	######## ATTRIBUTES #######
	##       Lst coords      ##
	###########################

	def __init__ (self, initiator) :
		if(isinstance(initiator, int)):
			self.coords = [0] * initiator;
		elif(isinstance(initiator, list)):
			self.coords = initiator;
		else :
			return "Invalid initiating parameter type."

	def __getitem__(self, j):
		return self.coords[j]

	def __setitem__(self, j, val) :
		self.coords[j] = val 

	def __str__(self) :
		return '<'+ str(self.coords)[1:-1] + '>'

	def __repr__ (self) :
		out = '<'
		for val in self.coords:
			out += str(val) + ','
		out = out[:-1];
		out += '>'
		return out;

	def __add__(self, other) :
		if (len(self) != len(other)):
			raise ValueError('dimensions must agree');
			result = Vector(len(self))

		for j in range(len(self)):
			result[j] = self[j] + other[j]
			return result 

	def __eq__(self, other) :
		return self.coords == other.coords
	
	def __ne__(self, other) :
		return not (self == other)

	def __sub__(self, other) :
		if (len(self.coords) == len(other.coords)) :
			outArr = [self.coords[i] - other.coords[i] for i in range(len(self.coords))];
			return Vector(outArr);
		else :
			#Vector Dimension Error
			raise ValueError('dimensions must agree');
			result = Vector(len(self))

	def __neg__(self) :
		outArr = [-i for i in self.coords];
		return Vector(outArr);

	def __mul__(self, other) :
		if(isinstance(other, int)) :
			return Vector([i*other for i in self.coords])
		if(isinstance(other, Vector)) :
			if (len(self.coords) == len(other.coords)) :
				return sum([self.coords[i] * other.coords[i] for i in range(len(self.coords))]);
			else :
				#Vector Dimension Error
				raise ValueError('dimensions must agree');
				result = Vector(len(self))

	def __rmul__(self, other) :
		if(isinstance(other, int)) :
			return Vector([i*other for i in self.coords])



#Testing
#vd = Vector([1,2]);
#v1 = Vector([1,2,3]);
#print(str(v1));
#v2 = Vector([4,5,6]);
#vs = v1-v2;
#print(vs);
#vn = -vs
#print(vn)

#vm = 3*v1;
#print(vm);
#vm = v1*3;
#print(vm);
#vm = v1 * v2;
#print(vm);

