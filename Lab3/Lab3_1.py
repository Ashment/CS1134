
def reverse_vowels(inStr) :
	#For Condition Reference
	vowelLst = ['a', 'e', 'i', 'o', 'u']

	#Build List
	inLst = [];
	for char in inStr :
		inLst.append(char);
	#O(n)

	#Build Vowel Index List
	vowelIndLst = [];
	for index in range(len(inLst)) :
		if(inLst[index] in vowelLst) :
			vowelIndLst.append(index);
	#O(n)

	#Reverse Vowel Positions
	for i in range(len(vowelIndLst)//2) :
		inLst[vowelIndLst[i]],inLst[vowelIndLst[(len(vowelIndLst)-1-i)]] = inLst[vowelIndLst[(len(vowelIndLst)-1-i)]],inLst[vowelIndLst[i]];
	#O(k)


	return ''.join(inLst);
	#O(n)
#Function Time Complexity : O(n)

strT = 'tandon'
print(reverse_vowels(strT));