class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbeg(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.next=self.head
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
            self.tail.next=self.head
    def insertend(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.next=self.head
        else:
            temp=node(data)
            self.tail.next=temp
            self.tail=temp
            self.tail.next=self.head
    def insertmid(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
            self.head.next=self.head
        else:
            ptr=self.head
            length=self.length()
            count=length//2
            while(count>1):
                count-=1
                ptr=ptr.next
            temp=node(data)
            temp.next=ptr.next
            ptr.next=temp
    def deletebeg(self):
        if(self.head==None):
            print('Empty Linked List')
        elif(self.head==self.tail):
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
    def deleteend(self):
        if(self.head==None):
            print('Empty Linked List')
        elif(self.head==self.tail):
            self.head=self.tail=None
        else:
            ptr=self.head
            while(1):
                if(ptr.next.next==self.head):
                    ptr.next=self.head
                    return
                ptr=ptr.next
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
            ptr.next=ptr.next.next
    def reverse(self):
        if(self.head==None):
            print('Empty linked list')
        elif(self.head==self.tail):return
        else:
            p1=self.head
            p2=p1.next
            p3=None
            while(p2!=self.head):
                p1.next=p3
                p3=p2.next
                p2.next=p1
                p1,p2,p3=p2,p3,p1
            self.head,self.tail=self.tail,self.head
            self.tail.next=self.head
    def length(self):
        if(self.head==None):return 0
        cnt=0
        ptr=self.head
        while(1):
            ptr=ptr.next
            cnt+=1
            if(ptr==self.head):return cnt
    def traverse(self):
        if(self.head==None):
            print('Empty linked list')
        else:
            ptr=self.head
            while(1):
                print(ptr.data,end=' ')
                ptr=ptr.next
                if(ptr==self.head):break
            print()
ll=CircularLinkedList()
ll.insertend(1)
ll.insertend(2)
ll.insertend(3)
ll.insertend(4)
ll.insertend(5)
ll.traverse()
ll.insertbeg(0)
ll.insertend(6)
ll.traverse()
ll.deletebeg()
ll.deleteend()
ll.traverse()
