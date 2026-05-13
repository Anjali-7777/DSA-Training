# python interpreter is python virtual machine. 
# #String Slicing

# name="Anjali" #0 1 2 3 4 5
# print(name[0]) #A
# print(name[1]) #n   
# print(name[-1]) #j
# print(name[5]) #Anj
# print(name[0:5]) #Anj
# print(name[0:]) #Anjali
# print(name[:4]) #Anj
# print(name[:]) #Anjali
# print(name[1:4:2]) #Aja
# print(name[::-1]) #Aja 

# s = "Python is high level programming language"
# print(s.lower()) #python is high level programming language
# print(s.upper()) #PYTHON IS HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.swapcase()) #pYTHON IS HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.capitalize()) #Python is high level programming language
# print(s.title()) #Python Is High Level Programming Language

#%c and %d is known as access/format specifier
# name = "Anjali"
# age = 22
# salary = 50000
# print("{}   age is  {} salary is {}".format(name, age, salary)) #Anjali is 22 years old and his salary is 50000
# print("{0}  age is {1} salary is  {2}".format(name, age, salary)) #
# print("{x}  age is {y} salary is  {z}".format(x=name, y=age, z=salary)) #Anjali is 22 years old and his salary is 50000
# A=1
# print(f"{A} is a good girl") 

# name = "Anjali"
# for i in name:
#     print(i)

# i/p = "Prashant"
#o/p = "Prashnt"
#write a program to remove the duplicate characters from the strings = "Prashant"
# s="Prashant"
# new_s=""
# for i in s:
#     if i not in new_s:
#         new_s+=i    
# print(new_s)

#  #reverse the new string
# reverse_s=""
# for i in new_s:
#     reverse_s=i+reverse_s
# print(reverse_s)

# N=len(new_s)
# for i in range(N-1,-1,-1):
#     print(new_s[i],end="")

#Check for palindrome
#write a program to check whether the string is palindrome or not
#Logic: Use loops to compare the first and last characters of the string, then move towards the center until all characters are compared or a mismatch is found.
#Sample Input:"racecar"

# s="racecar"
# reverse_s=""
# for i in s:
#     reverse_s=i+reverse_s
# print(reverse_s)
# if s==reverse_s:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

# name= "help4code"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#         print("The string is a palindrome") 
# else:
#     print("The string is not a palindrome")

#Check for Anagram
#write a program to check whether the two strings are anagrams or not
# logic:Check if the characters of both strings are the same and in the same frequency. You can use a dictionary to count the frequency of each character in both strings and then compare the dictionaries.
#Sample Input: "listen" and "silent"
# s2="listen"
# s1="silent"
# s1_dict={}
# s2_dict={}
# for i in s1:
#     if i in s1_dict:
#         s1_dict[i] += 1
#     else:
#         s1_dict[i] = 1
# for i in s2:
#     if i in s2_dict:
#         s2_dict[i] += 1
#     else:
#         s2_dict[i] = 1
# if s1_dict == s2_dict:
#     print("The strings are anagrams")
# else:
#     print("The strings are not anagrams")

# #Vowels and Consonants
# #write a program to count the number of vowels and consonants in a string
# #Logic: Iterate through the string and check if each character is a vowel or a consonant
# vowels = "aeiouAEIOU"
# name= "Hello World"
# vowel = 0
# consonant= 0
# for i in name:
#     if i in vowels:
#         vowel += 1
#     else:
#         consonant += 1
# print("Number of vowels:", vowel)
# print("Number of consonants:", consonant)

#pangram
#write a program to check whether the string is pangram or not
#Logic:Use Loops to check if all letters are present.
# s = "The quick brown fox jumps over the lazy dog"

#Count Words in a String
#write a program to count the number of words in a string
#Logic: Use loops to count spaces and words
#Sample Input:"This is a sentence"
# s = "This is a sentence"
# word = 1
# for i in s:
#     if i == " ":
#         word += 1
# print("Number of words:", word)

#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#SecretMessage 
#input:gasgg54@#vscsdls and output:4
#Write a program to help the agency find the number of special characters and white spaces in the given string.
# s = "gasgg54@#vscsdls"
# special_characters = 0
# white_spaces = 0
# for i in s:
#     if i.isalnum():
#         continue
#     elif i.isspace():
#         white_spaces += 1
#     else:
#         special_characters += 1

# print("Number of special characters:", special_characters)
# print("Number of white spaces:", white_spaces)

#var ='gasgg54@#vscsd!s*'
#count = 0
#z =ord(i)
#print(z)
#if (z>=65 and z<=90) or (z>=97 and z<=122) or (z>=48 and z<=57):
#    continue
#else:
#    count += 1

#Title Case a Sentence
#write a program to convert the first letter of each word in a sentence to uppercase and the rest of the letters to lowercase
#Logic split the sentence into words, then capitalize the first letter of each word and join them back together.
#Sample Input:"this is a test"
# s = "this is a test"
# print(s.title())

# print('Anjali7777' .isalnum())
# print('AnjaliPatalbansi' .isalpha())
# print('123fg' .isdigit())
# print('ssbyfc' .islower())
# print('' .islower())
# print('ANJAali' .isupper())
# print('My Name is Anjali' .istitle())
# print(' ' .isspace())
# print(''.istitle())
# print("Hello" .startswith("He"))
# print("Hello" .endswith("lo"))

# print("AnjaliPatalbansi" .find("tal"))
# print("AnjaliPatalbansi" .index("tal"))
# print("AnjaliPatalbansi" .count("z"))

# 1 1 1
# 2 2 2
# 3 3 3
#for i in range (1,4)::
#     for j in range(1,4):
#         print(i,end=" ")
#     print()   
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1, 1+i):
#         print("*",end=" ")
#     print()

# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+i),end=" ")
#     print()

# from anyio import sleep

# import time
# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, 1+i):
#         sleep(1)
#         print("*",end=" ")
#     print()

#Product of Array Except Self
#Sample Input: [1,2,3,4]
#Excepted Output: [24,12,8,6]
#Logic: Use two passes ,one from left to right and one from right to left,calculate the products.
arr= [1,2,3,4]
product = 1
for i in arr:
 product=product*i
for i in range(0,len(arr)):
    arr[i]=product//arr[i]
print(arr)
  
