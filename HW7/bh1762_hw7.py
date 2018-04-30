
class EmptyTree (Exception):
    pass

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum


    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return 0
        elif (subtree_root.left is not None):
            return 1 + self.subtree_height(subtree_root.left)
        elif (subtree_root.right is not None):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def __iter__(self):
        for node in self.postorder():
            yield node.data



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


    
    ### QUESTION 2 ###
    def leaves_list(self):
        if(self.root is None):
            return [];
        #    raise EmptyTree(' /!\ Tree is empty /!\ ')
        print("Generating list...")
        return list(self.find_leaves(self.root));


    def find_leaves(self, curRoot):

        if (curRoot.left is None) and (curRoot.right is None):
            print('Leaf node reached.')
            yield curRoot.data;
        else :
#            print(curRoot.left.data, curRoot.right.data);
            if(curRoot.left != None):
                print('Recursively finding leaves on left.')
                yield from self.find_leaves(curRoot.left);
            if(curRoot.right != None):
                print('Recursively finding leaves on right.')
                yield from self.find_leaves(curRoot.right);

    ### QUESTION 4 ###
    def iterative_inorder(self):
        curN = self.root;

        while curN is not None:
            if(curN.left is None):
                yield curN.data;
                curN = curN.right;
            else:
                curL = curN.left;

                while(curL.right is not None) and (curL.right is not curN):
                    curL = curL.right

                if(curL.right is None) :
                    curL.right = curN;
                    curN = curN.left;
                else:
                    curL.right = None;
                    yield curN.data;
                    curN = curN.right;


### QUESTION 1 ###
def min_and_max(bin_tree):
    print("Initiating find min max function.")
    if(bin_tree.root is None):
        raise EmptyTree(" /!\ Tree is empty /!\ ");
    return subtree_min_and_max(bin_tree.root);


def subtree_min_and_max(curRoot):

    print("Running on Root Node... Data >", curRoot.data);
    if(curRoot.left != None):
        #Recursively run function on left subtree.
        nextRoot = subtree_min_and_max(curRoot.left);
        if(curRoot.data < nextRoot[0]):
            LMin = curRoot.data;
            LMax = nextRoot[1];
        elif(curRoot.data > nextRoot[1]):
            LMax = curRoot.data;
            LMin = nextRoot[0];
        else:
            LMin = nextRoot[0];
            LMax = nextRoot[1];

        #If no other subtree, return.
        if(curRoot.right == None):
            return (LMin, LMax);

    if(curRoot.right != None):
        #Recursively run function on right subtree.
        nextRoot = subtree_min_and_max(curRoot.right);
        if(curRoot.data < nextRoot[0]):
            RMin = curRoot.data;
            RMax = nextRoot[1];
        elif(curRoot.data > nextRoot[1]):
            RMax = curRoot.data;
            RMin = nextRoot[0];
        else:
            RMin = nextRoot[0];
            RMax = nextRoot[1];

        #If no other subtree, return.
        if(curRoot.left == None):
            print("Leaf node reached.")
            return (RMin, RMax);

    #Code is here if there are either two or none subtrees.
    if(curRoot.left==None and curRoot.right==None):
        #At this point, if there are no subtrees, return.
        print("Leaf Node Reached.")
        return (curRoot.data, curRoot.data);
    else:
        #Otherise, compare two subtree results and return final output.
        if(LMin < RMin):
            outMin = LMin;
        else:
            outMin = RMin;
        if(LMax > RMax):
            outMax = LMax;
        else:
            outMax = RMax;

        return (outMin, outMax);



### QUESTION 3 ###
def is_height_balanced(binTree):
    print("Now Checking Height Balance");
    return subtree_balanced(binTree, binTree.root)[0];


def subtree_balanced(bTree, curRoot):
    print("Checking Balance from sub-root...");
    if(curRoot is None):
        #Leaf Node
        return (True, 0);
    else:
        #At least one child
        leftCall = subtree_balanced(bTree, curRoot.left);
        rightCall = subtree_balanced(bTree, curRoot.right)
        if(leftCall[0] and rightCall[0]):
            #Check left and right height.
            curHeight = max(leftCall[1], rightCall[1]);
            if(abs(leftCall[1] - rightCall[1]) > 1):
                print("Unbalanced Subtree Found.");
                return False, curHeight + 1;
            else:
                print("Balanced Subtree.")
                return True, curHeight + 1;

        else:
            #Unbalanced somewhere. return False.
            return False, 0;


### QUESTION 5 ###
def create_expression_tree(preExpStr):
    expLst = list(tokens(preExpStr));
    return LinkedBinaryTree((expression_subtree_gen(expLst, 0))[0]);

def expression_subtree_gen(preExpLst, curInd):
    if(curInd >= len(preExpLst)):
        return

    else:
        #Construct Root
        n = preExpLst[curInd];
        print("N >", preExpLst[curInd]);
        curInd += 1;

        #Construct Left Child.
        print("Constructing Left Child.")
        if(type(preExpLst[curInd]) == int):
            #If next node is number, create node.
            print("Next is number >", preExpLst[curInd]);
            l = LinkedBinaryTree.Node(preExpLst[curInd]);
            curInd += 1;
            nInd = curInd
        else:
            #If left node not number, create subtree.
            print("Next is operation. Recursive call >")
            next = expression_subtree_gen(preExpLst, curInd)
            l = next[0];
            nInd = next[1];

        print("current nInd =", nInd);

        print("Constructing Right Child.")
        if(type(preExpLst[nInd]) == int):
            print("Next is number >", preExpLst[nInd])
            r = LinkedBinaryTree.Node(preExpLst[nInd]);
            nInd += 1;
        else:
            print("Next is operation. Recursive call >")
            r = expression_subtree_gen(preExpLst, nInd)[0]


        print("VVVSubtree Construction CompleteVVV");
        return (LinkedBinaryTree.Node(n, l, r), nInd);

def prefix_to_postfix(preExpStr):
    preTree = create_expression_tree(preExpStr);
    pLst = [];
    for e in preTree.postorder():
        pLst.append(str(e.data));
    return ' '.join(pLst);


def tokens(exp_str):
    exp_str = exp_str.strip()
    n = len(exp_str)
    i = 0

    while(i < n):
        #skipping spaces
        while(exp_str[i] == ' '):
            i += 1
        if (exp_str[i] in "+-*/"):
            yield exp_str[i]
            i += 1
        else:
            digits_list = []
            while (i<n and exp_str[i].isdigit()):
                digits_list.append(exp_str[i])
                i += 1
            yield int(''.join(digits_list));
                



def DEBUG():
    n1 = LinkedBinaryTree.Node(1);
    n2 = LinkedBinaryTree.Node(2);
    n3 = LinkedBinaryTree.Node(3, n1, n2);
    n4 = LinkedBinaryTree.Node(4);
    n5 = LinkedBinaryTree.Node(5);
    n6 = LinkedBinaryTree.Node(6, n4, n5);
    rt = LinkedBinaryTree.Node(10, n3, n6);

    bbTree = LinkedBinaryTree(rt);
    empTree = LinkedBinaryTree();


    print(" >> Finding Min and Max << ")
    print(min_and_max(bbTree));
    print()

    print(" >> Listing Leaf Nodes << ")
    print(bbTree.leaves_list());
    print()

    print(" >> Interative Inorder << ")
    print(list(bbTree.iterative_inorder()));
    print()

    print(" >> Prefix Expression Tree << ")
    print(create_expression_tree('* 2 + - 15 6 4'))




#DEBUG();















