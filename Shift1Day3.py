#18:Maximum Consecutive Ones:
# arr = [1,1,0,1,1,1,0,1,1,1,1]
# count = 0
# max_count=0
# for i in arr:
#     if i == 1:
#         count +=1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

#Count Substrings in a String:TCSPattern Question
# str = "abababab"
# substr = "ab"
# count = 0

# for i in str:
#     if i == substr:
#         count += 1
# else:
#     count = 0
# print(count)

# loop with slicing
s = "abababab"
# substr = "ab"
# count = 0

# for i in range(len(s) - len(substr) + 1):
#     if s[i:i+len(substr)] == substr:
#         count += 1

# print(count)  # Output: 4

# s = "abababab"
# substr = "ab"
# count = s.count(substr)
# print(count)  # Output: 4




#while loop
# i = 1
# while i<=5: 
#     print(i)
#     i+= 1

#function

# def hello(): #called function
#     print("hello world")

# hello() #calling function
# hello()

# def arithmatic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# result =arithmatic()
# print("Arithmatic =",result)

#How many types of argument we pass in function?
#1.Positional argument
#2.keyword argument
#3.Default arguemnt
#4.Variable length argument / variable number of the argument

# def arithmatic(a,b):
  
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# result =arithmatic(5,5)
# print("Arithmatic =",result)

#keyword argument
# def credential(username, password):
#     if username == password:
#         print("login sucessfully")
#     else:
#         print("invalid credentials")

# credential(username="admin", password="admin")

#default argument
# def cityName(city = "Pune"):
#     print(city)

# cityName("Nagpur")
# cityName("Mumbai")
# cityName()

#Variable length
# def cityName(*name):
#     print(name)
# cityName("Nagpur","delhi","Mumbai","pune")

#modularity approach
# import sys
# def add():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a+b)
# def sub():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a-b)

# def mul():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a*b)
# def div():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a/b)

# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Division")
#     print("4.Multiplication")
#     print("5.Exit")
#     choice=int(input("Enter your choice:"))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5 :
#          sys.exit()
    

#//DSA//
# def findBiggestNumber(sampleArray): #[5,7,9,2,3,4] ======>
#     biggestNumber =  sampleArray#biggestNumber = 5   O(1)
#     for index in range(1,len(sampleArray)):#index =1   O(N)
        
#         if sampleArray[index] > biggestNumber:   #O(1)
#             biggestNumber =  sampleArray[index]   #O(1)
#             print(biggestNumber)                    #O(1)

# sampleArray = [5,7,9,2,3,4]                     #========>
# findBiggestNumber(sampleArray)                   #========>

#O(1)+O(1)+O(1)+O(1)+O(N)=O(N)

# def count_substrings(s, substr):
#     count = 0
#     for i in range(len(s) - len(substr) + 1):
#         if s[i:i+len(substr)] == substr:
#             count += 1
#     return count

# # Example usage
# string = "abababab"
# substring = "ab"
# result = count_substrings(string, substring)
# print(f"'{substring}' occurs {result} times in '{string}'")

