#Default Constructor
# # class Name:
#     age = 30
#     def display(self):
#         print("Hello World")

# obj = Name()
# print(obj.age)
# obj.display()


# class Student:
#     def __init__(self):
#         self.name ="prashant"
#         self.age =30

#     def display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)
# stuObj = Student()
# print(stuObj)

# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")

# obj = Message()        
# obj.show()
# obj2 = Message()

#Parmeterized Constructor
# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no
#     def dsiplayStudentInfo(self):
#         print("Name",self.Name)
#         print("Age=",self.Age)

# studentobj = StudentInfo("Prakash",34,101) 
# studentobj.dsiplayStudentInfo()

import sys
class Stack:
    def __init__(self, size):
        self.myStack =[]
        self.stackSize = size

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            False    

    def push(self,value):
        if self.isFull():
            print("Stack is full")
        else:
         self.myStack.append(value)
        print("Element push")

    def display(self):
        print(self.myStack)
    
    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
    
    def  pop(self):
        if self .isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])

    def deleteStack(self):
        self.myStack =  None
size = int(input("Enter the size of stack :")) 
obj = Stack(size)
while True:
   
    print("Stack has created :")
    print("1.Push Operation:")
    print("2.Print Stack")
    print("3.Pop Operation")
    print("4.Peek Operation")
    print("5.Delete Stack")
    print("6.Exit")
    choice =int(input("Enter Your Choice:"))        
    if choice == 1:
        value = int(input("Enter value to push in stack :"))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif  choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice ==5:
        obj.deleteStack()
    else:
        sys.exit()

