import sys
sys.setrecursionlimit(10**6+99)

class Queue:
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue(self,data):
        self.instack.append(data)
    def dequeue(self):
        if(not self.outstack):
            while(self.instack):
                item=self.instack.pop()
                self.outstack.append(item)
        return self.outstack.pop()

capacity=int(input('Enter size of queue - '))
q=Queue(capacity)
d={
    0:'exit',
    1:'enqueue',
    2:'dequeue',
}
while(1):
    choice=int(input('enter choice - '))
    try:
        print('you opt to {}'.format(d[choice]))
        if(choice==1):
            data=int(input('enter data - '))
            q.enqueue(data)
        elif(choice==2):
            item=q.dequeue()
        else:
            sys.exit()
    except:print('Invalid Choice')
    print()