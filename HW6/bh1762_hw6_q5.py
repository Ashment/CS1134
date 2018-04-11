
#################################################
##### D   I   S   C   L   A   I   M   E   R #####
#################################################
### Even though the homework instructions ask ###
### the homework questions be submitted as two ##
### separate files, the only way the autograder #
### is willing to accept an answer is if the  ###
### classes are pasted here. So here it is.   ###
### Piazza offered no productive answer,      ###
### stating that there is precedent for auto- ###
### grader giving all test case pass. Well,   ###
### here is the only way to get it to pass.   ###
### Thanks instructor for answering the       ###
### on Piazza!                                ###
#################################################


class Empty (Exception) :
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"



#################################################
##### D   I   S   C   L   A   I   M   E   R #####
#################################################
######### PLEASE READ DISCLAIMER AT TOP #########
### QUESTION RELEVANT CODE STARTS HERE. #########



def merge_linked_lists(srtlst1, srtlst2) :
    print("MERGING |>", srtlst1, srtlst2);
    h1 = srtlst1.header.next
    h2 = srtlst2.header.next
    return merge_sublists(srtlst1, srtlst2, h1, h2, DoublyLinkedList());



def merge_sublists(srtlst1, srtlst2, cNode1, cNode2, outLst):

    print("MERGE SUBLIST |>", cNode1.data, '|' ,cNode2.data)

    if(cNode1 is srtlst1.trailer) and (cNode2 is srtlst2.trailer) :
        return outLst;
    else :
        if (cNode2 is srtlst2.trailer):
            outLst.add_last(cNode1.data);
            return merge_sublists(srtlst1, srtlst2, cNode1.next, cNode2, outLst);
        elif (cNode1 is srtlst1.trailer) :
            outLst.add_last(cNode2.data);
            return merge_sublists(srtlst1, srtlst2, cNode1, cNode2.next, outLst);
        elif(cNode1.data <= cNode2.data):
            outLst.add_last(cNode1.data);
            return merge_sublists(srtlst1, srtlst2, cNode1.next, cNode2, outLst);
        elif(cNode2.data < cNode1.data) :
            outLst.add_last(cNode2.data);
            return merge_sublists(srtlst1, srtlst2, cNode1, cNode2.next, outLst);






























