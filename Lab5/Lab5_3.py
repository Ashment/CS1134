

def isPalindrome(instr) :
	if(len(instr) <= 1) :
		return True

	if(instr[0] == instr[len(instr)-1]):
		print(instr[1:len(instr)-1])
		return isPalindrome(instr[1:len(instr)-1]);
	else :
		return False


palin = 'kayak'
nopalin = 'what'
palin2 = 'racecar'

print(isPalindrome(palin))
print(isPalindrome(nopalin))
print(isPalindrome(palin2))