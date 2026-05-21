# class Node:
#     def __init__(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 
#     def __str__(self):
#         return str(self.info) 

# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

#     def create(self, val):  
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
         
#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break

# """
# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)
# """
# def inOrder(root):
#     if root:
#         inOrder(root.left)
#         print(root.info,end = " ")
#         inOrder(root.right)



# tree = BinarySearchTree()
# t = int(input())

# arr = list(map(int, input().split()))

# for i in range(t):
#     tree.create(arr[i])

# inOrder(tree.root)

# class Node:
#     def __init__(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     def __str__(self):
#         return str(self.info) 

# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

#     def create(self, val):  
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
         
#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break

# """
# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)
# """
# def preOrder(root):
#     #Write your code here
#      if root:
#            print(root.info  , end=" ")
#            preOrder(root.left)
#            preOrder(root.right)


# tree = BinarySearchTree()
# t = int(input())

# arr = list(map(int, input().split()))

# for i in range(t):
#     tree.create(arr[i])

# preOrder(tree.root)

# class Node:
#     def __init__(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     def __str__(self):
#         return str(self.info) 

# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

#     def create(self, val):  
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
#          while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break
#                 """
# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)
# """
# def postOrder(root):
#     if root:
    
#          postOrder(root.left)
#          postOrder(root.right)
#          print(root.info,end = " ")

#Large amount of data: to increase performance :we use stack using linkedlist


#push(method):

# class Node:
#     def __init__(self,value = None):
#         self.values =  value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode  #  in generator we use yeild to return value (sequntially)
#             curNode = curNode.next
# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()
    
#     def __str__(self):
#         values = [str(x.values) for x in self.LinkedList]
#         return '\n'.join(values)

    
#     def isEmpty(self):
#         if self.LinkedList.head == None:
#             return True
#         else:
#             return False
        

#     def push(self,value):
#         node =Node(value)
#         node.next = self.LinkedList.head
#         self.LinkedList.head = node

#     def pop(self):
#         if self.isEmpty():
#             return"There is no any element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.values
#             self.LinkedList.head = self.LinkedList.head.next
#             return nodeValue

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.values
#             return nodeValue
    

# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# print("Display Top Value: ")
# print(customStack.peek())
# print("Pop top element")
# print(customStack.pop())
# print("Now check the stack again")
# print(customStack)
# print("Pop top element")
# print(customStack)


class Node:
    def __init__(self, value=None):
       self.value = value
       self.next = None
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
         self.head = None
         self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode  #  in generator we use yeild to return value (sequntially)
            curNode = curNode.next
class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    
        
    def enqueue(self,value):
        newNode =Node(value)
        if self.LinkedList.head == None:
          self.LinkedList.head = newNode
          self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return"There is no any node in the queue"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
              self.LinkedList.head = None
              self.LinkedList.tail = None
            else:
                self.LinkedList.head =  self.LinkedList.head.next
            return tempNode


    def peek(self):
        if self.isEmpty():
            return "There is not any node in the stack"
        else:
            return self.LinkedList.head
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

    

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("Display Top Value: ")
print(customQueue.peek())
print("Delete FIFO Manner ")
print(customQueue.dequeue())
print("Display Queue again")
print(customQueue)



    
        