


def InvertedTree(Tree):
	invTree = LinkedBinaryTree(Tree.root);
	InvertSubtree(Tree.root, invTree);
	return invTree;


def InvertedSubtree(sTree, newTree):
	if ((sTree.left == None) and (sTree.right == None)):
		#Return current node if leaf node.
		return sTree;

	sTr = None;
	sTl = None;
	#Invert children of subtrees if not none.
	if((sTree.left != None)):
		sTl = InvertSubtree(sTree.left, newTree.left);
	if((sTree.right != None)):
		sTr = InvertSubtree((sTree.right, newTree.right));

	#Swap left and right subtrees.
	newTree.left, newTree.right = sTl, sTr;
	return newTree;