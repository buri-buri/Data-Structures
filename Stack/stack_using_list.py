import sys
sys.setrecursionlimit(10**6+99)

class Stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        if(self.stack==[]):return True
        return False
    def push(self,data):
        self.stack.append(data)
        return
    def pop(self):
        if(not self.isempty()):
            item=self.stack.pop()
            return item
        else:
            print('Empty Stack')
            return
    def peek(self):
        if(not self.isempty()):
            return self.stack[-1]
        else:
            print('Empty Stack')
    def traverse(self):
        if(not self.isempty()):
            print(*self.stack)
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
