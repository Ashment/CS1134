def is_bst(binary_tree):
	return is_bst_helper(binary_tree.root)[0];

def is_bst_helper(curRoot):
	cur = curRoot.data;
	if(curRoot.left is None) and (curRoot.right is None):
		return (True, cur, cur);
	else:		
		if(curRoot.left is None):
			lMin = cur;
			lMax = cur;
		else:
			leftNext = is_bst_helper(curRoot.left);
			if(leftNext[0] == False):
				return (False, 0, 0);
			lMin = leftNext[1];
			lMax = leftNext[2];
		if(curRoot.right is None):
			rMin = cur;
			rMax = cur;
		else:
			rightNext = is_bst_helper(curRoot.right);
			if(rightNext[0] == False):
				return (False, 0, 0);
			rMin = rightNext[1];
			rMax = rightNext[2];

		if(lMax > rMin) or (lMax > cur) or (rMin < cur):
			return (False, 0, 0);
		else:
			return (True, lMin, rMax);
			