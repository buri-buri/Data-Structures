import sys
sys.setrecursionlimit(10**6+99)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbeg(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
    def insertend(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
        else:
            temp=node(data)
            self.tail.next=temp
            self.tail=temp
    def insertmid(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
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
    def deleteend(self):
        if(self.head==None):
            print('Empty Linked List')
        elif(self.head==self.tail):
            self.head=self.tail=None
        else:
            ptr=self.head
            while(1):
                if(ptr.next.next==None):
                    ptr.next=None
                    return
                ptr=ptr.next
                self.tail=ptr
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
            while(p2):
                p1.next=p3
                p3=p2.next
                p2.next=p1
                p1,p2,p3=p2,p3,p1
            self.head,self.tail=self.tail,self.head
    def length(self):
        cnt=0
        ptr=self.head
        while(ptr):
            ptr=ptr.next
            cnt+=1
        return cnt
    def find_mid(self):
        if(self.head==None):
            print('Empty Linked List')
            return
        slow=fast=self.head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def traverse(self):
        if(self.head==None):
            print('Empty linked list')
            return
        ptr=self.head
        while(ptr):
            print(ptr.data,end=' ')
            ptr=ptr.next
        print()

ll=LinkedList()
d={
    0:'exit',
    11:'insertbeg',
    12:'insertmid',
    13:'insertend',
    21:'deletebeg',
    22:'deletemid',
    23:'deleteend',
    3:'reverse',
    4:'findmid',
    5:'traverse'
}
while(1):
    choice=int(input('enter choice - '))
    try:print('you opt to {}'.format(d[choice]))
    except:print('Invalid Choice')

    if(choice>10 and choice<14):
        data=int(input('enter data - '))
        if(choice==11):ll.insertbeg(data)
        elif(choice==12):ll.insertmid(data)
        else:ll.insertend(data)

    if(choice>20 and choice<24):
        if(choice==21):ll.deletebeg()
        elif(choice==22):ll.deletemid()
        else:ll.deleteend()

    elif(choice==3):
        ll.reverse()
    elif(choice==4):
        ll.find_mid()
    elif(choice==5):
        ll.traverse()
    else:
        if(choice==0):
            sys.exit()
    print()
