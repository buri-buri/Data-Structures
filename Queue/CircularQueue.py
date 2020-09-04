import sys
sys.setrecursionlimit(10**6+99)

class Queue:
    def __init__(self,capacity):
        self.head=None
    

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