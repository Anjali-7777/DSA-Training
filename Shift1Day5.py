#Wipro imp que
# import math

# stack = [79, 77, 54, 81, 48, 34, 25, 16]

# count = 0

# while stack:
#     area = stack.pop()

#     if math.isqrt(area) ** 2 == area:
#         count += 1

# print(count)

# Q.what is the output of the code(MCQ)

# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v) 
# print(t,v[0])   

# #MCQ
# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     #return values
# f(1)  #calling function
# f(2)
# f(3)

#Queue DS:-
#1.Enqueue
#2.Dequeue
#display

# import sys
# class Queue:
#     def  __init__(self, size):
#         self.myQueue =[]
#         self.queuesize = size
    
#     def isFull(self):
#         if len(self.myQueue) ==size:
#             return True
#         else:
#             return False
        
#     def enQueue(self,value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)

#     def display(self):
#         print(self.myQueue)

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False
        
#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue[0])
    
#     def deleteQueue(self):
#         self.myQueue=None
 
# size = int(input("Enter the size of Queue:"))
# obj = Queue(size)
# print("Stack has created:")
# while True:
#     print("1.Enqueue operation : ")
#     print("2.Display Queue : ")
#     print("3. delete operation : ")
#     print("4. Peek operation : ")
#     print("5. Delete Queue : ")
#     print("6. Exit")
#     choice =  int(input("Enter Your choice :"))
#     if choice == 1:
#      value = int(input("Enter element to add in Queue: "))
#      obj.enQueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.deQueue()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteQueue()
#     elif choice == 6:
#         sys.exit()
    
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

#Write a program to accept student name and marks from the keyboard
#and creates a dictionary.Also display student marks by taking student name

# n = int(input("Enter the number of Students: "))
# d = {}
# for i in range(n):
#     name = input("Enter Student Name:")
#     marks = input("Enter Student Marks:")
#     d[name]=marks
# while True:
#     name=input("Enter Student Name to get Marks:")
#     marks=d.get(name,-1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("The Marks of",name,"are",marks)
#     option=input("Do you want to find another student marks[Yes|No]")
#     if option == "No":
#         break
#     print("Thanks for using our application")    

#Write a program to access each chapter of string in forward and backward direction by using while loop
#i/p ="Learning Python is very easy"

s = "Learning Python is very easy"
for i in s(0,len-1):
    print(i)
    for j in s (-1,0):
        print(j)