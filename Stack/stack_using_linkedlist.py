import sys
sys.setrecursionlimit(10**6+99)

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if(self.head==None):return True
        return False
    def push(self,data):
        if(self.head==None):
            self.head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
            return
    def pop(self):
        if(not self.isempty()):
            popnode=self.head
            self.head=self.head.next
            popnode.next=None
            return popnode.data
        else:
            print('Empty Stack')
            return
    def peek(self):
        if(not self.isempty()):
            return self.head.data
        else:
            print('Empty Stack')
            return 
    def traverse(self):
        if(not self.isempty()):
            ptr=self.head
            while(ptr):
                print(ptr.data,end=' ')
                ptr=ptr.next
            print()
        else:
            print('Empty Stack')
            return
s=Stack()
d={
    0:'exit',
    1:'push',
    2:'pop',
    3:'peek',
    4:'traverse'
}
while(1):
    choice=int(input('enter choice - '))
    try:
        print('you opt to {}'.format(d[choice]))
        if(choice==1):
            data=int(input('enter data - '))
            s.push(data)
        elif(choice==2):
            item=s.pop()
        elif(choice==3):
            item=s.peek()
            if(item):
                print('top of stack is',item)
        elif(choice==4):
            s.traverse()
        else:
            sys.exit()
    except:print('Invalid Choice')
    print()
