
###############################################################
###            R E S O U R C E       C L A S S              ###
###############################################################


class BinarySearchTreeMap:

    def get_ith_smallest(self, ii):
        if(ii > len(self)):
            raise IndexError("/!\ ith element out of range.");
        else:
            return self.find_ith_smallest(self.root, ii);

    def find_ith_smallest(self, curRoot, ii):
        curVal = curRoot.item.key;
        if(ii == curRoot.lSubSize + 1):
            return curVal;
        else :
            if(ii <= curRoot.lSubSize):
                return self.find_ith_smallest(curRoot.left, ii);
            else:
                return self.find_ith_smallest(curRoot.right, ii - 1 - curRoot.lSubSize);

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
            self.lSubSize = 0;

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
            curParent = parent;
            curChild = new_node;
            while curParent is not None:
                if curParent.left is curChild:
                    curParent.lSubSize += 1;
                curChild = curParent;
                curParent = curChild.parent;


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
                curChild = max_of_left;
                curParent = curChild.parent;
                while curr_parent is not None:
                    if curParent.left is curChild:
                        curParent.lSubSize -= 1;
                    curChild = curParent;
                    curParent = curChild.parent;
                self.subtree_delete(node_to_delete.left, max_of_left.item.key);

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                curChild = node_to_delete;
                curParent = curChild.parent;
                while curr_parent is not None:
                    if curParent.left is curChild:
                        curParent.lSubSize -= 1;
                    curChild = curParent;
                    curParent = curChild.parent;
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
                curParent = parent;
                curChild = child;
                while curParent is not None:
                    if curParent.left is curChild:
                        curParent.lSubSize -= 1
                    curChild = curParent;
                    curParent = curChild.parent;

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                curChild = max_of_left;
                curParent = curChild.parent;
                while curr_parent is not None:
                    if curParent.left is curChild:
                        curParent.lSubSize -= 1;
                    curChild = curParent;
                    curParent = curChild.parent;
                self.subtree_delete(node_to_delete.left, max_of_left.item.key);

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