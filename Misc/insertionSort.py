#insertion sort

def insertion_sort(A):
	""" sort list of comparable elements into non-decreasing order"""
    for k in range(1, len(A)):
    	print('- - -');
    	curr = A[k]          # current element to be inserted
   		j = k               # begin to look for correct index j for curr

        while j > 0 and A[j-1] > curr:
        	A[j] = A[j-1]   # shift larger element, A[j-1] to the right
            j -= 1
            print(A);
            A[j] = curr         # either A[j-1] <= curr or j==0 and curr is smallest of all
            
Z = [4,3,2,5,1];
print(Z);
insertion_sort(Z);
print(Z);
