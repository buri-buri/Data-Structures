import sys
from collections import deque
sys.setrecursionlimit(10**6+99)
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if(self.root==None):
            self.root=node(data)
            self.q=deque([self.root])
        else:
            if(self.q[0].left):
                self.q[0].right=node(data)
                self.q.append(self.q[0].right)
                self.q.popleft()
            else:
                self.q[0].left=node(data)
                self.q.append(self.q[0].left)
    def delete(self,data):
        if(self.root==None):
            print('Empty Tree')
        else:
            rightmostnode=self.RightMostNode(self.root)
            parent=self.parentofanynode(self.root,rightmostnode.data)
            if(parent):parent.right=None
            node=self.findAnode(self.root,data)
            node.data=rightmostnode.data
    def height(self,node,cnt):
        if(node==None):
            return cnt
        return max(self.height(node.left,cnt+1),self.height(node.right,cnt+1))
    def preorder(self,node):
        if(node):
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self,node):
        if(node):
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def postorder(self,node):
        if(node):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
    def LevelOrderTraversal(self):
        if(self.root==None):
            print('Empty Tree')
        else:
            q=deque([self.root])
            while(q):
                node=q.popleft()
                print(node.data)
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
    def ZigZagTraversal(self):
        if(self.root==None):
            print('Empty Tree')
        else:
            turn='left'
            left=deque([self.root])
            right=deque([])
            height=self.height(self.root,0)
            while(height):
                if(turn=='left'):
                    while(left):
                        node=left.popleft()
                        print(node.data)
                        if(node.left):right.append(node.left)
                        if(node.right):right.append(node.right)
                    turn='right'
                else:
                    while(right):
                        node=right.pop()
                        print(node.data)
                        if(node.right):left.appendleft(node.right)
                        if(node.left):left.appendleft(node.left)
                    turn='left'
                height-=1
    def LeftMostNode(self,node):
        if(node.left==None):
            return node
        return self.LeftMostNode(node.left)
    def RightMostNode(self,node):
        if(node.right==None):
            return node
        return self.RightMostNode(node.right)
    def parentofanynode(self,node,data):
        if(node.left):
            if(node.left.data==data):
                return node
        if(node.right):
            if(node.right.data==data):
                return node
        if(node.left):
            curr_node=self.parentofanynode(node.left,data)
            if(curr_node):
                return curr_node
        if(node.right):
            curr_node=self.parentofanynode(node.right,data)
            if(curr_node):
                return curr_node
    def findAnode(self,node,data):
        if(node.data==data):
            return node
        if(node.left):
            curr_node=self.findAnode(node.left,data)
            if(curr_node):
                return curr_node
        if(node.right):
            curr_node=self.findAnode(node.right,data)
            if(curr_node):
                return curr_node
    def IsMirrorImage(self,lnode,rnode):
        if(lnode==None or rnode==None):
            if(lnode==rnode==None):
                return 1
            return 0
        if(lnode.data!=rnode.data):
            return 0
        return self.IsMirrorImage(lnode.left,lnode.right) * self.IsMirrorImage(rnode.left,rnode.right)
    def MirrorImage(self):
        if(self.root==None):
            print('Empty Tree')
        else:
            return self.IsMirrorImage(self.root.left,self.root.right)

t=tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(8)
t.insert(9)
t.insert(10)
t.insert(11)
t.insert(12)
t.insert(13)
t.insert(14)
t.insert(15)
t.LevelOrderTraversal()