# #Linear serach
# def linearSearch(array, target):    #O(N)
#     for i in range(0, len(array)):        #O(1)
#         if array[i] == target:    #O(1)
#             return i                  #O(1)

# array =[1,2,3,4,8,7,9]  #O(1)
# target = 7
# result = linearSearch(array, target)
# if result == -1:
#     print("Target value not found")
# else:
#     print("Element found at index",result )

    #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
# def solveMeFirst(a,b):
#    return a+b


# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)

# def simpleArraySum(ar):
#     sum = 0
#     for i in range(len(ar)):
#         sum = sum + ar[i]
#     return sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


#Removing spaces from the string
#rstrip() ==> To remove spaces at right hand side
#lstrip() ==> To remove spaces at left hand side
#strip() ==> To remove spaces both sides

# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hyderbad':
#     print("Hello Hyderbadi..Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi...Vanakkam")
# elif scity=="Banglore":
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("your entered city is invalid")

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     alice=0
#     bob=0
#     for i in range (3):
#         if a[i]>b[i]:
#             alice += 1
#         elif a[i]<b[i]:
#             bob += 1
#     return [alice,bob]
            
        
   

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'aVeryBigSum' function below.
# #
# # The function is expected to return a LONG_INTEGER.
# # The function accepts LONG_INTEGER_ARRAY ar as parameter.
# #

# def aVeryBigSum(ar):
#     # Write your code here
#     sum=0
#     for i in range (len(ar)):
#         sum=sum+ar[i]
#     return sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#Roy and Profile Picture
# L = int(input())
# N = int(input())

# for _ in range(N):
#     W, H = map(int, input().split())

#     if W < L or H < L:
#         print("UPLOAD ANOTHER")

#     elif W == H:
#         print("ACCEPTED")

#     else:
#         print("CROP IT")

# arr=[[100,198,333,323],
#       [122,232,221,111],
#       [223,565,245,764]]

# for i in arr:
# #     print(max(i))
# arr=[[100,198,333,323],
#       [122,232,221,111],
#       [223,565,245,764]]

# newlist=[]
# for i in range(len(arr)):
#     j=0
#     max = arr[i][j]
#     for j in range(len(arr)):
#         c_max =arr[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
#     print(newlist)

    
# s = "prashant*is*a*good*progrmmer"

# star = ""
# text = ""


# for ch in s:
#     if ch == '*':
#         star = star + ch
#     else:
#         text = text + ch


# result = star + text

# print(result)

str = 'aaabbbbccceeeee'
freq = {}

for ch in str:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
    


