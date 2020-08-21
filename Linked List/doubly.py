class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbeg(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.prev=self.tail.next=None
        else:
            temp=node(data)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def insertend(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.prev=self.tail.next=None
        else:
            temp=node(data)
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=temp
    def insertmid(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.prev=self.tail.next=None
        else:
            ptr=self.head
            length=self.length()
            count=length//2
            while(count>1):
                count-=1
                ptr=ptr.next
            temp=node(data)
            temp.next=ptr.next
            ptr.next.prev=temp
            ptr.next=temp
            temp.prev=ptr
    def deletebeg(self):
        if(self.head==None):
            print('Empty Linked List')
        elif(self.head==self.tail):
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev.next=None
            self.head.prev=None
    def deleteend(self):
        if(self.head==None):
            print('Empty Linked List')
        elif(self.head==self.tail):
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next.prev=None
            self.tail.next=None
    def deletemid(self):
        if(self.head==None):
            print('Empty Linked List')
        else:
            ptr=self.head
            lenght=self.length()
            count=lenght//2 + (1 if(lenght%2) else 0)
            ptr=self.head
            while(count>2):
                ptr=ptr.next
                count-=1
            ptr.next.prev=None
            ptr.next=ptr.next.next
            ptr.next.prev.next=None
            ptr.next.prev=ptr
    def reverse(self):
        if(self.head==None):
            print('Empty linked list')
        elif(self.head==self.tail):return
        else:
            p1=self.tail
            p2=self.tail.prev
            self.head.prev=self.head
            self.tail.prev=None
            while(p1!=p2):
                p1.next=p2
                p2.next=None
                p2=p2.prev
                p2.next=None
                p1.next.prev=p1
                p1=p1.next
            self.head,self.tail=self.tail,self.head
    def length(self):
        cnt=0
        ptr=self.head
        while(ptr):
            ptr=ptr.next
            cnt+=1
        return cnt
    def traverse(self):
        if(self.head==None):
            print('Empty linked list')
        else:
            ptr=self.head
            while(ptr):
                print(ptr.data,end=' ')
                ptr=ptr.next
            print()
ll=CircularLinkedList()
ll.insertend(1)
ll.insertend(2)
ll.insertend(3)
ll.insertend(4)
ll.insertend(5)
ll.traverse()
ll.traverse()
ll.insertbeg(0)
ll.insertend(6)
ll.reverse()
ll.traverse()