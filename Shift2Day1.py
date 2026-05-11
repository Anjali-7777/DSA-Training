#collection datatypes
#List Collection Datatype
# myList = ["anjali","Aditya","isha","Nikita",77,89.30,"Athrav","Sanchit","Ankit","Ayush"]
# print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[-1])
# print(myList[2:5])
# print(myList[1:])#start to end
# print(myList[:5])#start to end
# print(myList[1:8:2])#start to end with step

#mutable list
# myList[0] = "Lokesh"
# print(myList)

# if "anjali" in myList:
#     print("Anjali is present in the list")
# else:
#     print("Anjali is not present in the list")

# myList.append("Vidhan")
# myList.append("Isha")
# print(myList)#add element at the end of the list

# myList.insert(2,"Soham")
# print(myList)
# myList.remove("Soham")
# print(myList)   

# newList = myList.copy()
# print(newList)




# myList = [['anjali','patalbansi'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list:")
# print(myList)
# print(myList[row][column])
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][0]) 
# print(myList[2][0])
# print(myList[2][1])

# List2=[50,25.50,'anjali']
# # del List2
# del List2[1]#delete element at index 0
# print(List2)

# List2=[50,25.50,'anjali']
# List2.clear()#delete all elements from the list
# print(List2)

# name="Anjali"
# print(name)
# myList = list(name)
# myList.sort()
# print(myList)
# myList.reverse()
# print(myList)
# myList.sort(reverse=True)
# print(myList)

#Alising
myList = [1,2,3,4,5]
# newList = myList
# print(id(myList))
# print(id(newList))
# for i in myList:
#     print(i)
# i/p =[0,1,4,0,2,5]
# o/p =[1,4,2,5,0,0]
#input =[0,1,4,0,2,5] and output =[1,4,2,5,0,0] both are same but in different order
# inputList = [0,1,4,0,2,5]
# outputList = [1,4,2,5,0,0]  
# for i in inputList:
#     if i == 0:
#         outputList.remove(i)
#         outputList.append(i)
# print(outputList)
#Find the second  largest number in the list
#Question: Find the second largest number in the array
#sample Input: [7,3,9,2,8]
#Excepted Output : Second largest number is 8

# myList= [7,3,9,2,8]
# myList.sort()       
# print("Second largest number is",myList[-2])

#slicing
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5,]
# print(a[3:0:-1])

# arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr =  [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i -1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end=" ")  

# fruit_list1 = ["Apple","Berry","Cherry","Papaya"]
# fruit_list2= fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = "Guava"
# fruit_list3[1] = "Kiwi"

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == "Guava":
#         sum += 1
#         if ls[1] == "Kiwi":
#             sum += 20
#     print(sum)

#Find the Intersection of Three Arrays:
#Question:Find the common elements in three arrays
#Logic: Use three sets to keep track of common eleemnts between the arrays.
#Sample Input:[1,2,3],[2,3,4],[3,4,5]
#Excepted Output: [3]

# A= [1,2,3]
# B= [2,3,4]          
# C= [3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

# 
mylist = []

N = int(input("Enter the value of N: "))

for i in range(N):
    element = int(input("Enter an element: "))
    mylist.append(element)

print("The list is:", mylist)

sum = 0

for i in range(len(mylist) - 1):
    sum += abs(mylist[i] - mylist[i + 1])

print("Total distance:", sum)