import math

a = [10**i for i in range (8)];
print(a);
b = [sum([2*i for i in range (j+1)]) for j in range (10)];
print(b);
c = [chr(i) for i in range (ord('a'), ord('z')+1)];
print (c);