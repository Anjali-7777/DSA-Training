#Find all Duplicate in a List
# arr = [4,3,2,7,8,2,1,5,5]
# darr = []
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#       if arr[i] == arr[j] and i not in darr:
#         darr.append(arr[i])
# print(darr)

#sort the dictionary

#instance variable seperate memory space for different object

# class New:
#     def __init__(self):
#         self.a = 10

# Obj1 = New()
# Obj2 = New()
# obj3 = New()
# Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(obj3.a)

# class New:
#     a = 10

#     def __init__(self):
#         self.name = "parshant"
# Obj1 =  New()
# Obj2 =  New()
# Obj3 = New()
# New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#for every object a seprate copy of instance variable created but in case of static

#variable only one copy will be created and it is accessble for every object of the I

#class

# class College:
#     collegename= "Modern College" #static variable (1 memory)

#     def __init__ (self):

#       self.studentname = "prashant" #instance varible (3 seprate memory)

# principal = College() # object creation

# teacher = College()

# accountant = College()

# print("principal=", principal.collegename, "....", principal.studentname)

# print("teacher =", teacher.collegename, teacher.studentname)

# print("accountant=", accountant.collegename, "....", accountant.studentname)

# College.collegename="HBD" # second way to add static variable

# principal.studentname="prashant jha"

# print("principal=", principal.collegename, "|", principal.studentname)

# print("teacher =", teacher.collegename, "|", teacher.studentname)

# print("accountant=", accountant.collegename, "", accountant.studentname)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next =  None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# Linkedlist = LinkedList()
# Linkedlist.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# #connecting a node
# Linkedlist.head.next = second
# second.next = third
# third.next = fourth

# #display linkedlist
# while Linkedlist.head.next != None:
#     print(Linkedlist.head.data,"|","->",end="")
#     Linkedlist.head = Linkedlist.head.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addNodeatBeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # if list was empty
            self.tail = new_node

    def addNodeatEnd(self, data):
        self.addNode(data)  # reuse addNode

    def addNodeinBetween(self, data):
        pos = int(input("Enter position after which to insert: "))
        temp = self.head
        count = 1
        while temp is not None and count < pos:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position not found")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            if temp == self.tail:  # update tail if inserted at end
                self.tail = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

if __name__ == '__main__':
    ll = LinkedList()
    while True:
        print('\n1. Add Node Linkedlist :')
        print('2. Add Node in Beginning :')
        print('3. Add Node in Between :')
        print('4. Add Node in End  :')
        print('5. Display Linked List :')
        print('6. Exit')
        ch = int(input('Enter your choice :'))
        if ch == 1:
            value = int(input('Enter value for node:'))
            ll.addNode(value)
            print('Node added successfully.')
        elif ch == 2:
            value = int(input('Enter value for node:'))
            ll.addNodeatBeg(value)
            print('Node added successfully.')
        elif ch == 3:
            value = int(input('Enter value for node:'))
            ll.addNodeinBetween(value)
            print('Node added successfully.')
        elif ch == 4:
            value = int(input('Enter value for node:'))
            ll.addNodeatEnd(value)
            print('Node added successfully.')
        elif ch == 5:
            ll.display()
        elif ch == 6:
            break
        else:
            print('Invalid choice')


 