
#Write a program to access each chapter of string in forward and backward direction by using while loop
#i/p ="Learning Python is very easy"
# s="learning python is very easy"
# i=0
# print("Forward direction")

# while i < len(s):
#     print(s[i],end="")
#     i+=1
    
# i = len(s) - 1
# print("\nBackward Direction:")

# while i >= 0:
#     print(s[i], end="")
#     i -= 1
# Input strings
# data = "abcdfjgerj abcdfijger"


# for i in range(len(data)):
    
#     # Check for space
#     if data[i] == " ":
        
#         # Print previous character
#         print(data[i-1])

# v = ['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels:")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print('Unique vowels',len(found),'from the given word=',w)


# x,y,z = map(int,input().split())
# mylist =[]
# for i in range(x):
#     a = int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end='')

# import datetime

# date=datetime.datetime.now()
# print("It's now:{:%d/%m/%Y/%H:%M:%S}".format(date))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# val=[2**i for i in range(1,6)]
# print(val)

# val[i*i for i in range(1,11)]
# print(s)

#list comprehension
# sqaures={x:x*x for x in range(1,6)}
# print(sqaures)

#dictionary comprehension
# doubles ={x:2*x for x in range(1,6)}
# print(doubles)


#How to read multiple line input in single line input
# a,b= [int(x) for x in input("Enter 2 numbers:").split()]
# print("Product is:",a*b)

# a,b,c = [float(x) for x in input("Enter 3 float numbers:").split(',')]
# print("The Sum is:",a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")



# while True:
#     username=input("Enter username:")
#     password=input("Enter password:")
#     if username == 'admin' and password == "admin":
#         print("login")
#         break
#     else:
#         print("Invalid")    
   
#Tower of Hanoi
import time
class Tower:
    def __init__(self):
        print("Welcome to Tower of Hanoi Game")
        print()
        print("Given Problem  A=[3,2,1]     B= []    C[]")
        print()
        print("Expected Output A= []    B=[]    C[3,2,1]")
        self.A = []
        self.B = []
        self.C = []
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
    def pass1(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass One Completed====================\n")

    def pass2(self):
        self.temp = self.A.pop()
        self.B.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Two Completed====================\n")

    def pass3(self):
        self.temp = self.C.pop()
        self.B.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Three Completed====================\n")

    def pass4(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Four Completed====================\n")

    def pass5(self):
        self.temp = self.B.pop()
        self.A.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Five Completed====================\n")

    def pass6(self):
        self.temp = self.B.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Six Completed====================\n")

    def pass7(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Seven Completed====================\n")
obj =  Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()