# s = "leetcode"
# x= []
# for i in range(0,len(s)):
#     if s[i] not in x:
#         x.append(s[i])
#     else:
#         x.remove(s[i])
# print(x[0])

# #recursion uses stack memory
# #when the main porobelm can be divided into trhe sub problem , when we used the recusrion?

# #factorial selection
# def factorial(num):
#     if num <=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))

# #captialFirst Selection using recursion

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0: 
#         return result                                       #  012
#     result.append(arr[0][0].upper() + arr[0][1:])         #0   car
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))


# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# def productofArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0]*productofArray(arr[1:])
# print(productofArray([1,2,3]))
# print(productofArray([1,2,3,10]))

#reverse a string using recursion

# def reverse(string):
#     if len(string) <= 1:
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])
# print(reverse('python'))
# print(reverse('appliers'))

# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return str(num) + str(recursiveRange(num -1))

# print(recursiveRange(6))

# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome('awesome'))

# def someRecursive(arr ,cb):
#     if len(arr)  ==  0 :
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True
# def isOdd(num):
#     if num %2 == 0:
#         return False
#     else:
#         return True
    
# print(someRecursive([1,2,3,4], isOdd))
# print(someRecursive([4,5,6,7], isOdd))
# print(someRecursive([4,6,8], isOdd))

    