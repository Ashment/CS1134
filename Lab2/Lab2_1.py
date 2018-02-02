import random

def roll_the_dice_str(n):
	s = ""
	for i in range(1, n+1):									#ϴ(n)
		curr_val = random.randint(1, 6)						#ϴ(1)
		s = s + str(curr_val) + " "							#ϴ(n)
	return s[:-1]
															#Function Run Time: ϴ(n²)

def roll_the_dice_str_lin(n):
	results = [random.randint(1,6) for i in range(n)]:		#ϴ(n)
	return ' '.join(results);								#ϴ(n)
															#Function Run Time: ϴ(2n) = ϴ(n)

