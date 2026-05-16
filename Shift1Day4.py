# #input = aaabbbbccceeeee
# #output = a3b4c3e5
# name = 'aabbbbeeeeffggg'
# newname ={}
# for i in range(len(name)):
#     key = name[i]
#     count=0
#     for j in range(len(name)):
#         if key == name[j]:
#             count+=1
#     newname[key] = count
# print(newname)
# for i,j in newname.items():
#     print(i,j,sep='',end='')


# salary = int(input('Enter your salary :'))
# rating = int(input('Enter your performance appraisal rating :'))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increment=salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment =salary*40/100
# else:
#     print('Invalid rating')
# print('Increment Salary:',increment+salary)


# basicSalary = 20000
# HRA=0
# TA=0
# DA=0
# Gross_Salary =0

# HRA = basicSalary *20/100
# TA = basicSalary*30/100
# DA = basicSalary*45/100

# Gross_Salary = HRA+TA+DA+basicSalary
# print(Gross_Salary)

# def binarySearch(array, target):
#     low = 0
#     high = len(array)-1
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target: 
#             low = mid+1
#         else:
#             high = mid-1
#     return -1        



# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result = binarySearch(array, target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at",result)


# #LeetcodeBinary Search
# class Solution(object):
#     def search(self, nums, target):
#         low = 0
#         high = len(nums) - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if nums[mid] == target:
        #         return mid

        #     elif nums[mid] < target:
        #         low = mid + 1

        #     else:
        #         high = mid - 1

        # return -1

#Bubble Sort
# def bubbleSort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 temp =nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j]=temp
#             print(nums)
#         print()

# nums = [64,34,25,12,22,11,90]
# bubbleSort(nums)

# def bubbleSort(nums):
#     count = 0
#     nums=578378923
#     nums(map(int,str(nums)))

#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j] == nums[j+1]:
#                 count = nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j]=count
#             print(nums)
#         print()
    

mylist= [5,7,8,3,7,8,9,2,3]
newlist=[]

for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=i+1
    while j<len(mylist):
        if key == mylist[j]:
            newlist.append(key)
        j=j+1
print(len(newlist))       
print(newlist)         


 

