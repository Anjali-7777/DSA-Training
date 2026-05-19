# #Reverse Each word in a string
# s = "Hi I'm Anjali"
# reversed_words = " ".join(word[::-1] for word in s.split())
# print(reversed_words)

#Check for valid Parentheses
# s = "({[]})"
# stack = []
# valid = True

# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if len(stack) == 0:
#             valid = False
#             break
#         top = stack.pop()
#         if ch == ')' and top != '(':
#             valid = False
#             break
#         elif ch == '}' and top != '{':
#             valid = False
#             break
#         elif ch == ']' and top != '[':
#             valid = False
#             break

# if len(stack) != 0:
#     valid = False

# if valid:
#     print("Valid")
# else:
#     print("Invalid")

#Sort ythe List 

# arr = [5,3,8,6,2]
# for i in  range (1,len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j]>key:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j + 1] = key
#     print(arr)
# print (arr)

# Selection sort in Python


# def selectionSort(array, size):
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
         
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
         
#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])


# data = [-2, 45, 0, 11, -9]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)


arr = [20,12,10,15,2]
for i in range(len(arr)):
    min = i
    j= i+1

    while j < len(arr):
        if arr[j]<arr[min]:
         min = j
    j = j+1
    print(arr)

    arr[i],arr[min]=arr[min],arr[i]
    print(arr)
print(arr)

#Array rotation 


