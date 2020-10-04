class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def list_traversal(self):
        itr=self.head
        while(itr):
            print(itr.data)
            itr=itr.next
    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,self.head)
            self.head=node
            return
        itr = self.head
        while (itr.next):
            itr = itr.next

        node=Node(data,None)
        itr.next=node
    def insert_values(self,values):
        #self.head=None
        for value in values:
            self.insert_at_end(value)
    def get_length(self):
        itr=self.head
        count=0
        while(itr):
            count+=1
            itr=itr.next
        return count
    def remove_at_index(self,index):
        count=0
        itr=self.head
        if index<0 or index>= self.get_length():
            print("Invalid Index")
            return
        if index==0:
            self.head=self.head.next
            return
        while(itr):
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_at_index(self,data,index):
        if index<0 or index>self.get_length():
            print("Invalid index")
            return
        if index==0:
            self.insert_at_beginning(data)
            return
        if index==self.get_length():
            self.insert_at_end(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr=self.head
        count=0
        while itr:
            if itr.data==data_after:
                self.insert_at_index(data_to_insert, count+1)
                break
            count+=1
            itr=itr.next

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at_index(count)
                break
            count += 1
            itr = itr.next



# Search for first occurance of data_after value in linked list
# Now insert data_to_insert after data_after nod




if __name__=="__main__":
    """
    l=LinkedList()
    l.insert_at_beginning(6)
    l.insert_at_beginning(6)
    l.insert_at_end(7)
    l.insert_values(["I","AM","A","PROGRAMMER"])
    l.list_traversal()
    l.remove_at_index(5)
    l.list_traversal()
    l.insert_at_index("A",5)
    l.list_traversal()
   """
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.list_traversal()
    print("----------")
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.list_traversal()
    print("----------")
    ll.remove_by_value("orange") # remove orange from linked list
    ll.list_traversal()
    print("----------")
    ll.remove_by_value("figs")
    ll.list_traversal()
    print("----------")
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.list_traversal()

