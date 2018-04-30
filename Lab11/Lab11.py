


#1
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



#2
def SubtreeChildrenDistance(sTree, cList=[0,0,0]):
	if((self.left == None) and (self.right == None)):
		#Leaf node.
		cList[0] += 1;
		return cList;

	if(self.left != None):
		SubtreeChildrenDistance(sTree.left, cList);
		if(self.right == None):
			#Left child only.
			cList[1] += 1;
		else :
			#Both children.
			cList[2] += 1;
			SubtreeChildrenDistance(sTree.right, cList);
	else:
		#Right child only.
		cList[1] += 1;
		SubtreeChildrenDistance(sTree.right, cList);

	return cList



#3
def FlattenTree(Tree):
	return FlattenSubtree(Tree.root);



def FlattenSubtree(sTree):
	if((sTree.left == None) and (sTree.right == None)):
		#Return leaf node.
		return sTree;

	if(sTree.left != None):
		#only left child

	else:
		#Only right child





























