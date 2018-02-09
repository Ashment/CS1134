import math
import random
import time

def FillWithRandInt(n) :
	results = [random.randint(-1000,1000) for i in range(n)];
	return results;


class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()



class PolynomialRep :

	######## ATTRIBUTES #######
	##       Lst coeffs      ##
	###########################

	def __init__ (self, coeffsIn) :

		if(not coeffsIn == []) :
			self.coeffs = coeffsIn;
		else :
			self.coeffs = [0];


	def __repr__ (self) :
		curPow = str(len(self.coeffs)-1)
		out = "";
		if self.coeffs[(len(self.coeffs))-1] < 0 :
			out += '-'	
		out += str(abs(self.coeffs[(len(self.coeffs))-1])) + 'x' if abs(self.coeffs[(len(self.coeffs))-1]) != 0 else 'x';
		out += self.toSuperscript(curPow);

		for i in range(len(self.coeffs)-2, -1, -1) :
			if(self.coeffs[i] != 0) :
				curPow = str(i);
				if(i<0) :
					out += ' - '
				else :
					out += ' + '
				out += str(abs(self.coeffs[i])) if abs(self.coeffs[i])>1 else '';
				out += 'x' if int(curPow)>0 else '';
				out += self.toSuperscript(curPow) if int(curPow)>1 else '';

		return out;

	def toSuperscript(self, strIn) :
		#YEAAAHHHH UNICODE!
		uniSuperLst = ['\u2070','\u00b9', '\u00b3','\u00b2','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079'];

		out = '';
		for char in strIn :
			out += uniSuperLst[int(char)];
		return out;

	def Eval(self, valIn) :
		out = 0.0;
		for i in range(0, len(self.coeffs)) :
			out += self.coeffs[i] * (valIn**i);
		return out;


	def __add__ (self, other) :
		while (len(self.coeffs) < len(other.coeffs)) :
			self.coeffs.append(0);
		while (len(other.coeffs) < len(self.coeffs)) :
			other.coeffs.append(0);
		out = [0 for i in range(len(self.coeffs))];

		for i in range(len(self.coeffs)) :
			out[i] = self.coeffs[i] + other.coeffs[i];

		return PolynomialRep(out);


	def __mul__ (self, other) :
		out = [0 for i in range((len(self.coeffs)) + (len(other.coeffs)))]
		for i in range(len(self.coeffs)) :
			for j in range(len(other.coeffs)) :
				out[i+j] += self.coeffs[i] * other.coeffs[j];
		#print(out);
		return PolynomialRep(out);


	def Derive(self) :
		for i in range(1, len(self.coeffs)) :
			self.coeffs[i-1] = self.coeffs[i] * i;
		#print(self);


filledLists = [FillWithRandInt(100), FillWithRandInt(200), FillWithRandInt(500), FillWithRandInt(1000), FillWithRandInt(10000)];
sizeLst = [100,200,500,1000,10000];
timer = PolyTimer();

f = open('./evalTime.csv', 'w');
f.write('Degree,InitTime,EvalTime,AddTime,MultTime,DeriveTime\n');

for i in range(len(filledLists)) :
	timer.reset();
	poly = PolynomialRep(filledLists[i]);
	iTime = timer.elapsed();

	timer.reset();
	poly.Eval(1);
	eTime = timer.elapsed();

	timer.reset();
	poly.Derive();
	dTime = timer.elapsed();

	temp = PolynomialRep(filledLists[i]);

	timer.reset();
	poly + temp;
	aTime = timer.elapsed();

	timer.reset();
	poly * temp;
	mTime = timer.elapsed();


	f.write(str(sizeLst[i]) + ',' + str(iTime) + ',' + str(eTime) + ',' + str(aTime) + ',' + str(mTime) + ',' + str(dTime) + '\n');

f.close();




##################################################	
##################################################
## polyT = PolynomialRep([0,1,3,0,1,0,0,0,2]);	##
## polyTo = PolynomialRep([3,0,5])				##
## 												##
## print(polyT);								##
##												##
## print(polyTo);								##							
## 												##
## print(polyT + polyTo);						##
##												##
## print(polyT * polyTo);						##
##												##
## polyT.Derive();								##
##################################################
##################################################	























