
def e_approx(n) :
	curSum = 0;
	curDenom = 1;

	for i in range (1, n+2) :
		curSum += 1/curDenom;
		curDenom *= i;

	return curSum;


def main():
	for n in range(15):
		curr_approx = e_approx(n)
		approx_str = "{:.15f}".format(curr_approx)
		print("n =", n, "Approximation:", approx_str)

#main();