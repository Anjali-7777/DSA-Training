#Tree is non linear data structure
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = [] 

#     def __str__(self, level = 0):
#         rat = "    "* level + str(self.data)  + "\n"
#         for ch in self.child:
#             rat += ch. __str__(level+1)
#         return rat

#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree node added")

# rootNode = Tree("Drinks")
# Hot    = Tree("Hot")
# Cold   = Tree("Cold")
# Tea    = Tree("Tea")
# Coffee = Tree("Coffee")
# NonAlcoholic = Tree("Non Alcoholic")
# Alcoholic  = Tree("Alcoholic")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)

# print(rootNode)


# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = [] 

#     def __str__(self, level = 0):
#         rat = "    "* level + str(self.data)  + "\n"
#         for ch in self.child:
#             rat += ch. __str__(level+1)
#         return rat

#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree node added")

# rootNode = Tree("N1")
# N2    = Tree("N2")
# N3 = Tree("N3")
# N4    = Tree("N4")
# N5 = Tree("N5")
# N6  = Tree("N6")
# N7  = Tree("N7")
# N8  = Tree("N8")
# N0 = Tree (" ")

# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N0)
# N3.addChild(N6)
# N4.addChild(N7)
# N5.addChild(N8)


# print(rootNode)

#recursive-digit-sum/problem
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'superDigit' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. STRING n
# #  2. INTEGER k
# #

# def superDigit(n, k):
    
#     # Sum of digits of n
#     total = sum(int(digit) for digit in n) * k
    
#     # Recursive function to find super digit
#     def find_super(num):
#         if num < 10:
#             return num
        
#         digit_sum = 0
#         while num > 0:
#             digit_sum += num % 10
#             num //= 10
        
#         return find_super(digit_sum)
    
#     return find_super(total)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = first_multiple_input[0]

#     k = int(first_multiple_input[1])

#     result = superDigit(n, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#https://leetcode.com/problems/sort-colors/

# class Solution:
#     def sortColors(self, nums):
#         # Step 1: Count frequencies of 0, 1, and 2
#         counts = [0, 0, 0]
#         for num in nums:
#             counts[num] += 1
        
#         # Step 2: Overwrite the array using the counts
#         index = 0
#         for color in range(3):
#             for _ in range(counts[color]):
#                 nums[index] = color
#                 index += 1

#https://www.hackerrank.com/challenges/insertionsort1/problem

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'insertionSort1' function below.
# #
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER_ARRAY arr
# #

# def insertionSort1(n, arr):

#     value = arr[-1]      # Last element to insert
#     i = n - 2

#     while i >= 0 and arr[i] > value:
#         arr[i + 1] = arr[i]
#         print(*arr)
#         i -= 1

#     arr[i + 1] = value
#     print(*arr)


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort1(n, arr)
