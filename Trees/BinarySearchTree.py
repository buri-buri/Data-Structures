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
        else:
            curr_node=self.root
            while(1):
                if(data>=curr_node.data):
                    if(curr_node.right==None):
                        curr_node.right=node(data)
                        break
                    curr_node=curr_node.right
                else:
                    if(curr_node.left==None):
                        curr_node.left=node(data)
                        break
                    curr_node=curr_node.left
    def delete(self,root,data):
        if(self.root==None):
            print('Empty Tree')
        else:
            node=root
            while(1):
                if(data<node.data):
                    node=node.left
                elif(data>node.data):
                    node=node.right
                else:
                    if(node.left is None and node.right is None):
                        node=None
                    elif(node.left and node.right is None):
                        node=node.left
                    elif(node.right and node.left is None):
                        node=node.right
                    else:
                        curr_node=node.right
                        while(curr_node.left):
                            curr_node=curr_node.left
                        node.data=curr_node.data
                        self.delete(node.right,curr_node.data)
                    break
    def inorder(self,node):
        if(node):
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def findAnode(self,node,data):
        if(node.data==data):
            return node
        if(node.left and node.left.data>data):
            return self.findAnode(node.left,data)
        if(node.right and node.right.data<data):
            return self.findAnode(node.right,data)

t=tree()
t.insert(50)
t.insert(25)
t.insert(85)
t.insert(15)
t.insert(30)
t.insert(75)
t.insert(90)
t.insert(10)
t.insert(8)
t.insert(12)
t.insert(45)
t.insert(28)
t.insert(60)
t.insert(70)
t.insert(65)
t.insert(72)
t.insert(88)
t.insert(80)
t.insert(100)

t.inorder(t.root)
t.delete(t.root,85)
print()
t.inorder(t.root)

'''
Deletion in BST arises 3 cases
    Case 1: deleting node is leaf node --> Chill Dude
    Case 2: deleting node has only 1 child --> No Problem
    Case 3: deleting node has 2 childs, here we have to find the "Inorder Successor" of curr node which is to be deleted
        Inorder Succesor means hum uss tree ka inorder print kre to hmari node kai just baad jo value aegi vo uss node ki inorder succesor hogi
    what i mean is ,let node(15) ka inorder successor find krna h
    and inorder traversal of whole tree is --> 1,3,7,8,10,15,17,20,25
    then yha (15) ka inorder successor 17 hoga and (15) ka inorder predecessor 10 hoga
        Actually in BST inorder successor means, uss subtree mai jo node hume delete krni hai, uss node se just badi value jo ki right hand side hi milegi
        samajh rhe hona, gien node se just badi value node to be deleted is 15, and inorder successor is 1,2,5,10,15,16,18,20
        to 16 hoga, and ye hmehsa Right_Hans pe hi milega due to the property of BST.
'''

