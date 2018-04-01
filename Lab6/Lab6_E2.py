#######################
##    HANOI PUZZLE   ##
#######################

def MoveDiskMsg(f, t) :
	return "Move disk from " + f + " to " + t;


def SolveHanoi(n, start, dest, spare) :
	if (n == 1):
		print(MoveDiskMsg(start, dest));
	else :
		SolveHanoi(n-1, start, spare, dest);
		print(MoveDiskMsg(start, dest));
		SolveHanoi(n-1, spare, dest, start);


SolveHanoi(3, 'A', 'C', 'B');