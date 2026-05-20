#Remove leading zeros from a list of integers
# Use list slicing or loops to remove zeros until a non zero element is encounttered
# list = [0,0,1,2,0,3,0,0,4]
# while list and list[0] == 0:
#     list.pop(0)
# print(list)

#Finding the first Missing postive integer
# arr=[3,4,-1,1]
# positive=set()

# for i in arr:
#     if i > 0:
#         positive.add(i)

# i=1
# while True:
#     if i not in positive:
#         print(i)
#         break
#     i +=1    

#find the smallest missing postitve integer:  INPUT:[7,8,9,11,12]

# arr=[7,8,9,11,12]
# positive=set(arr)
# i=1
# while True:
#     if i not in positive:
#         print(i)
#         break
#     i +=1

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data , end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end= " ")


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end= " ")
    inOrderTraversal(rootNode.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
          rootNode.leftChild.data == nodeValue
   
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None: 
            rootNode.rightChild.data == nodeValue
             
         
        else:
            searchNode(rootNode.rightChild,nodeValue)
    





newBST = BSTNode(None)
insertNode(newBST , 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
insertNode(newBST,10)
preOrderTraversal(newBST)
print()
inOrderTraversal(newBST)
print()
postOrderTraversal(newBST)



