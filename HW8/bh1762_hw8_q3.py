#import BinarySearchTreeMap


def restore_bst(preList):
	bTree = BinarySearchTreeMap();
	print("Restoring from list: ", preList);
	if(len(preList) > 0):
		bTree.root = restore_helper(preList, 0, preList[0]);
		print("Finished Tree Construction  >> ", bTree.root);
	return bTree;


def restore_helper(pList, curInd, rootNum):
	rootNode = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(pList[curInd]));
	curInd += 1
	if(curInd < len(pList)):
	#Build subtrees if not at end of list.
		print("- - - - - - BUILDING LEFT SUBTREE - - - - - -")
		print("curInd", curInd);
		leftSub = restore_helper_L(pList, curInd, rootNum);
		curInd = leftSub[1];
		
		print("- - - - - - BUILDING RIGHT SUBTREE - - - - - -")
		print("curInd", curInd);
		rightSub = restore_helper_R(pList, curInd, rootNum);

		rootNode.left = leftSub[0];
		rootNode.right = rightSub[0];

	return rootNode;


def restore_helper_L(pList, curInd, rootNum):
	curNode = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(pList[curInd]));
	oCurInd = curInd;
	print("\nCurrent Node Key :", curNode.item.key);
	curInd += 1;

	if(curInd < len(pList)):
	#Not yet at end of pList
		#BUILDING LEFT SIDE
		print("Checking index :", curInd);
		if(pList[curInd] < curNode.item.key):
		#Next number smaller than cur
			print("Building to left >", pList[curInd]);
			nextLeft = restore_helper_L(pList, curInd, curNode.item.key);
			curNode.left = nextLeft[0];
			curInd = nextLeft[1];
		else:
			print("Returning to branch, looking at :", pList[curInd]);
			return (curNode, curInd);

		#BUILDING RIGHT SIDE
		if(pList[curInd] > rootNum):
		#Next number is greater than current root
			print("Returning to root, looking at :", pList[curInd]);
			return (curNode, curInd);
		else: 
			print("Building to right >", pList[curInd]);
			rightN = restore_helper_L(pList, curInd, curNode.item.key);
			curNode.right = rightN[0];
			curInd = rightN[1];
			return(curNode, curInd);

	return (curNode, curInd);

def restore_helper_R(pList, curInd, rootNum):
	curNode = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(pList[curInd]));
	oCurInd = curInd;
	print("\nCurrent Node Key :", curNode.item.key);
	curInd += 1;

	if(curInd < len(pList)):
	#Not yet at end of pList
		#BUILDING LEFT SIDE
		print("Checking index :", curInd);
		if(pList[curInd] < curNode.item.key):
		#Next number smaller than cur
			print("Building to left >", pList[curInd]);
			nextLeft = restore_helper_R(pList, curInd, curNode.item.key);
			curNode.left = nextLeft[0];
			curInd = nextLeft[1];
		else:
			print("Returning to branch, looking at :", pList[curInd]);
			return (curNode, curInd);

		#BUILDING RIGHT SIDE
		if(curInd < len(pList)):
			#Still not at end of list.
			print("Building to right >", pList[curInd]);
			rightN = restore_helper_R(pList, curInd, curNode.item.key);
			curNode.right = rightN[0];
			curInd = rightN[1];
			return(curNode, curInd);

	return (curNode, curInd);



###############################################################
###            R E S O U R C E       C L A S S              ###
###############################################################


class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)