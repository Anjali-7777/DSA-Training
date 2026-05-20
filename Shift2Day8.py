# Complete the printLinkedList function below.

# #
# # For your reference:
# #
# # SinglyLinkedListNode:
# #     int data
# #     SinglyLinkedListNode next
# #
# #
# def printLinkedList(head):
#     current = head
    
#     while current is not None:
     
#        print(current.data) 
      
#        current = current.next
 
# if __name__ == '__main__':
#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)

#     printLinkedList(llist.head)

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

# 121. Best Time to Buy and Sell Stock
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max_profit = 0
#         for i in range(len(prices)):
#           for j in range(i+1,len(prices)):
#             profit = prices[j] - prices[i]
#             if profit>0:
#                 max_profit = max(max_profit,profit)

#         return max_profit

#9. Palindrome Number
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         # Negative numbers cannot be palindrome
#         if x < 0:
#             return False
        
#         original = x
#         reverse = 0
        
#         while x > 0:
#             digit = x % 10
#             reverse = reverse * 10 + digit
#             x //= 10
        
#         return original == reverse

#premutation
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
        
#         result = []

#         def backtrack(path, remaining):
            
#             # If no elements left, store permutation
#             if not remaining:
#                 result.append(path)
#                 return

#             # Try each element
#             for i in range(len(remaining)):
#                 backtrack(
#                     path + [remaining[i]],
#                     remaining[:i] + remaining[i+1:]
#                 )

#         backtrack([], nums)

#         return result


#combination sum

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """

#         result = []

#         def backtrack(start, path, total):

#             # If target achieved
#             if total == target:
#                 result.append(path[:])
#                 return

#             # If total exceeds target
#             if total > target:
#                 return

#             # Try each candidate
#             for i in range(start, len(candidates)):

#                 path.append(candidates[i])

#                 # Reuse same element -> pass i
#                 backtrack(i, path, total + candidates[i])

#                 # Backtrack
#                 path.pop()

#         backtrack(0, [], 0)

#         return result


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# try:
#      print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value :")
# except:
#     print("ABC")

# try:
#      a = int(input("Enter first number: "))
#      b = int(input("Enter second number: "))
#      print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value :")
# else:
#     print("Everything is ok")

# try:
#      a = int(input("Enter first number: "))
#      b = int(input("Enter second number: "))
#      print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value :")
# finally:
#     print("I always executed")

# import logging
# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no: "))
#     print(a/b)
# except(ZeroDivisionError,ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging Level is set up. Check 'newfile.txt' for log details.")
 
# import csv

# # open file in append mode
# f = open("employee.csv", 'a', newline='')  
# a = csv.writer(f)

# # Uncomment if you want to add headers once
# # a.writerow(["EmpID", "Emp Name", "Emp Age"])

# empid = int(input("Enter your Empid: "))
# empName = input("Enter employee name: ")
# age = int(input("Enter employee age: "))

# a.writerow([empid, empName, age])
# f.close()

# print("file is created")

#col name =studId | studName |phy|chem|math|Total|Percentage|Result
#input:studied ,studname,phy,chem,math
#check condition all paper marks >= 40 pass else fail

import csv
import os

# Check if file already exists
file_exists = os.path.isfile("student.csv")

# Open file in append mode
f = open("student.csv", "a", newline="")
a = csv.writer(f)

# Write header only once
if not file_exists:
    a.writerow(["studID", "studName", "Phy", "Chem", "Math",
                "Total", "Percentage", "Result"])

# Input from user
studID = int(input("Enter Student ID: "))
studName = input("Enter Student Name: ")

Phy = int(input("Enter Physics Marks: "))
Chem = int(input("Enter Chemistry Marks: "))
Math = int(input("Enter Maths Marks: "))

# Calculate total and percentage
Total = Phy + Chem + Math
Percentage = Total / 3

# Check pass/fail condition
if Phy >= 40 and Chem >= 40 and Math >= 40:
    Result = "PASS"
else:
    Result = "FAIL"

# Write data into CSV file
a.writerow([studID, studName, Phy, Chem, Math,
            Total, Percentage, Result])

# Close file
f.close()

print("Student record added successfully.")

