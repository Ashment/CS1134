import time
import random

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()


def FillWithRandInt(n) :
	results = [random.randint(-1000,1000) for i in range(n)];
	return results;


#-------------------------#
#timer = PolyTimer();     # 
#FillWithRandInt(1000000);#
#print (timer.elapsed()); #
#-------------------------#


def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0
    
    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0

    return maxSum, seqStart, seqEnd


'''
Quadratic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


'''
Cubic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


########################################################################
########################################################################
########################################################################


timer = PolyTimer();
p7 = FillWithRandInt(128);
p8 = FillWithRandInt(256);
p9 = FillWithRandInt(512);
p10 = FillWithRandInt(1024);
p11 = FillWithRandInt(2048);
p12 = FillWithRandInt(4096);
pList = [p7,p8,p9,p10,p11,p12];
print ('\nDuration for Random Filling : ')
print (timer.elapsed());
print ();

timer.reset();
result, start, end = maxSubsequenceSum1(p7);
print(timer.elapsed());


f = open('./Sum1.csv', 'w');
f.write('n, time\n')
for p in pList :
	timer.reset()
	result, start, end = maxSubsequenceSum1(p);
	f.write(str(len(p)) + ',' + str(timer.elapsed()) + '\n');
	print('\n' + 'DONE |> Sum1 : ' + str(len(p)) + '\n');
f.close();


f = open('./Sum2.csv', 'w');
f.write('n, time\n')
for p in pList :
	timer.reset()
	result, start, end = maxSubsequenceSum2(p);
	f.write(str(len(p)) + ',' + str(timer.elapsed()) + '\n');
	print('\n' + 'DONE |> Sum2 : ' + str(len(p)) + '\n');
f.close();


f = open('./Sum3.csv', 'w');
f.write('n, time\n')
for p in pList :
	timer.reset()
	result, start, end = maxSubsequenceSum3(p);
	f.write(str(len(p)) + ',' + str(timer.elapsed()) + '\n');
	print('\n' + 'DONE |> Sum3 : ' + str(len(p)) + '\n');
f.close();
















