import sys
sys.setrecursionlimit(10**6+99)

class Queue:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.maxsize=capacity
        self.front=self.rear=self.size=0
    def reset(self):
        self.front=self.rear=0
        self.queue=[None]*self.maxsize
    def isfull(self):
        return self.size==self.maxsize
    def isempty(self):
        return self.size==0
    def size_of_queue(self):
        return self.rear-self.front
    def enqueue(self,data):
        if(not self.isfull()):
            self.queue[self.rear]=data
            self.rear+=1
            self.size+=1
        else:
            print('Full Queue')
    def dequeue(self):
        if(not self.isempty()):
            item=self.queue[self.front]
            self.front+=1
            self.size-=1
            return item
        else:
            print('Empty Queue')
    def traverse(self):
        if(not self.isempty()):
            for i in range(self.front,self.rear):
                print(self.queue[i],end=' ')
            print()
        else:
            print('Empty Queue')

capacity=int(input('Enter size of queue - '))
q=Queue(capacity)
d={
    0:'exit',
    1:'enqueue',
    2:'dequeue',
    3:'traverse',
    4:'size_of_queue',
    5:'reset'
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
        elif(choice==3):
            q.traverse()
        elif(choice==4):
            size=q.size_of_queue()
            print(size)
        elif(choice==5):
            q.reset()
        else:
            sys.exit()
    except:print('Invalid Choice')
    print()
