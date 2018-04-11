import DoublyLinkedList

class CompactString :

    def __init__(self, oString='') :
        self.dataList = DoublyLinkedList.DoublyLinkedList();
        consec = 0;
        if(oString == '') :
            cur = ''
        else :
            cur = oString[0];
        for c in oString :
            if (c == cur) :
                consec += 1;
            else :
                self.dataList.add_last((cur, consec));
                cur = c;
                consec = 1;
        if(cur != '') :
            self.dataList.add_last((cur, consec));
            cur = c;
            consec = 1;

    def __add__(self, other) :
        #Create new empty compact string
        out = CompactString();

        sPointer = self.dataList.first_node();
        oPointer = other.dataList.first_node();
        #Add nodes from self except last
        for i in range(len(self.dataList)-1) :
            out.dataList.add_last(sPointer.data);
            sPointer = sPointer.next;
        #Detect and merge connecting node
        if(sPointer.data[0] == oPointer.data[0]) :
            mergeElement = (sPointer.data[0], sPointer.data[1] + oPointer.data[1]);
            out.dataList.add_last(mergeElement);
            oPointer = oPointer.next;
        #Add rest of nodes from other
        while oPointer is not other.dataList.trailer :
            out.dataList.add_last(oPointer.data);
            oPointer = oPointer.next;

        return out

    def __lt__ (self, other) :
        print("COMPARISON |> ", str(self), "<", str(other));
        curNodeS = self.dataList.header.next;
        curNodeO = other.dataList.header.next;

        #Building ordinal arrays for comparison
        ordListS = [];
        ordListO = [];
        while curNodeS is not self.dataList.trailer :
            for i in range(curNodeS.data[1]) :
                ordListS.append(ord(curNodeS.data[0]));
            curNodeS = curNodeS.next;
        while curNodeO is not other.dataList.trailer :
            for i in range(curNodeO.data[1]) :
                ordListO.append(ord(curNodeO.data[0]));
            curNodeO = curNodeO.next;

        if len(ordListO) == 0 :
            ordListO.append(0);
        if len(ordListS) == 0 :
            ordListS.append(0);


        cPointer = 0;
        while cPointer < len(ordListS) :
            #Other has run out of elements.
            if cPointer >= len(ordListO) :
                return False
            #If current comparison meets condition
            if ordListS[cPointer] < ordListO[cPointer] :
                return True
            elif ordListS[cPointer] > ordListO[cPointer] :
                return False
            cPointer += 1
        #Self has run out
        if(cPointer < len(ordListO)) :      
            return True;
        else :
            return False;

    def __le__ (self, other) :
        print("COMPARISON |> ", str(self), "<=", str(other));
        curNodeS = self.dataList.header.next;
        curNodeO = other.dataList.header.next;

        #Building ordinal arrays for comparison
        ordListS = [];
        ordListO = [];
        while curNodeS is not self.dataList.trailer :
            for i in range(curNodeS.data[1]) :
                ordListS.append(ord(curNodeS.data[0]));
            curNodeS = curNodeS.next;
        while curNodeO is not other.dataList.trailer :
            for i in range(curNodeO.data[1]) :
                ordListO.append(ord(curNodeO.data[0]));
            curNodeO = curNodeO.next;

        if len(ordListO) == 0 :
            ordListO.append(0);
        if len(ordListS) == 0 :
            ordListS.append(0);

        cPointer = 0;
        while cPointer < len(ordListS) :
            #Other has run out of elements.
            if cPointer >= len(ordListO) :
                return False
            #If current comparison meets condition
            if ordListS[cPointer] < ordListO[cPointer] :
                return True
            elif ordListS[cPointer] > ordListO[cPointer] :
                return False
            cPointer += 1
        #Self has run out
        if(cPointer == len(ordListO)) :      
            return True;
        else :
            return False;

    def __gt__ (self, other) :
        print("COMPARISON |> ", str(self), ">", str(other));
        curNodeS = self.dataList.header.next;
        curNodeO = other.dataList.header.next;

        #Building ordinal arrays for comparison
        ordListS = [];
        ordListO = [];
        while curNodeS is not self.dataList.trailer :
            for i in range(curNodeS.data[1]) :
                ordListS.append(ord(curNodeS.data[0]));
            curNodeS = curNodeS.next;
        while curNodeO is not other.dataList.trailer :
            for i in range(curNodeO.data[1]) :
                ordListO.append(ord(curNodeO.data[0]));
            curNodeO = curNodeO.next;

        if len(ordListO) == 0 :
            ordListO.append(0);
        if len(ordListS) == 0 :
            ordListS.append(0);

        cPointer = 0;
        while cPointer < len(ordListS) :
            #Other has run out of elements.
            if cPointer >= len(ordListO) :
                return True
            #If current comparison meets condition
            if ordListS[cPointer] > ordListO[cPointer] :
                return True
            elif ordListS[cPointer] < ordListO[cPointer] :
                return False
            cPointer += 1
        #Self has run out
        return False;

    def __ge__ (self, other) :
        print("COMPARISON |> ", str(self), ">=", str(other));
        curNodeS = self.dataList.header.next;
        curNodeO = other.dataList.header.next;

        #Building ordinal arrays for comparison
        ordListS = [];
        ordListO = [];
        while curNodeS is not self.dataList.trailer :
            for i in range(curNodeS.data[1]) :
                ordListS.append(ord(curNodeS.data[0]));
            curNodeS = curNodeS.next;
        while curNodeO is not other.dataList.trailer :
            for i in range(curNodeO.data[1]) :
                ordListO.append(ord(curNodeO.data[0]));
            curNodeO = curNodeO.next;

        if len(ordListO) == 0 :
            ordListO.append(0);
        if len(ordListS) == 0 :
            ordListS.append(0);

        cPointer = 0;
        while cPointer < len(ordListS) :
            #Other has run out of elements.
            if cPointer >= len(ordListO) :
                return True
            #If current comparison meets condition
            if ordListS[cPointer] > ordListO[cPointer] :
                return True
            elif ordListS[cPointer] < ordListO[cPointer] :
                return False
            cPointer += 1
        #Self has run out
        if(cPointer == len(ordListO)) :      
            return True;
        else :
            return False;




    def __repr__(self) :
        out = ''
        for e in self.dataList :
            out += (e[0])*(e[1]);
        return out;


def debug() :
    a = CompactString('free');
    b = CompactString('free');
    print(a <= b);


#debug();

















