
def print_triangle(n) :
	if (n>1) :
		print_triangle(n-1)
		print('*'*n);
	else :
		print('*');

def print_oposite_triangle(n) :
	if(n>1) :
		print('*'*n);
		print_oposite_triangle(n-1);
		print('*'*n);
	else :
		print('*\n*');

def print_ruler(n) :
	if(n == 1) :
		print('-');
	else :
		print_ruler(n-1);
		print('-'*n);
		print_ruler(n-1);