import DoublyLinkedList

def sum_lnk_lst(lnklst, n=None) :
    if(n == None):
        n = lnklst.header.next;

    if(n is lnklst.trailer) :
        return 0;
    else :
        return n.data + sum_lnk_lst(lnklst, n.next);


a = DoublyLinkedList.DoublyLinkedList();
a.add_last(1);
a.add_last(2);
a.add_last(3);
print(a);
print(sum_lnk_lst(a));