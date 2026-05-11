#why python is called dynamically typed language# age = 33
# pi = 3.14
# name = "Alice"
# result = True
# print (type(age))
# print (type(pi))
# print (type(name))
# print (type(result))

#why all fundmental data types are immutable 
# math = 50
# chem = 50
# phy = 50
# print(id(math))
# print(id(chem))
# print(id(phy))

# simple if 
# print(2+2)
# print("2"+"2")
# a = int(input("Enter  first number: "))#2 string concatination
# b = int(input("Enter  second number: "))#2
# print(a+b)

# print(int(3.14))#3
# #print(int(10+5j))
# print(int(True))#1
# print(int(False))#0
# print(int("4"))

#float()used to convert
# print(float(3))#3.0
# print(float(True))#1.0
# print(float(False))#0.0
# print(float(4.22))
# print(float("4"))

#complex() used to convert
# print(complex(3))#3+0j
# print(complex(12.5))#3.14+0j
# print(complex(True))#1+0j
# print(complex(False))#0+0j
# print(complex("5"))#4+0j
# print(complex("5.6"))#3+4j
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))

#bool() used to convert
# print(bool(0))#False
# print(bool(15))#True
# print(bool(3.14))#True
# print(bool(0.0))#False
# print(bool(1+2j))#False
# print(bool(0+0j))
# print(bool(-1))#False
# print(bool(False))#False
# print(bool(True))#True
#print(bool(""))#False


# #simple if
# a = int(input("Enter any single digit:"))
# if a >0:
#     print("Positive number")
# if a <0:
#     print("Negative number")    
# if a == 0:
#     print("Zero")

#if else
# day = input("Enter day of week:")
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
#   print("Working day")
# else:
#     print("Holiday")

#else if ladder
# per =65
# if per >=65:
#     print("Grade A")
# elif per <=65 and per >=50:
#     print("Grade B")   
# else:
#     print("Fail") 

# a = input("Enter anything:")
# if a.isdigit():
#     print("It is a number")
# elif a.islower():
#     print("It is a lowercase string")
# elif a.isupper():
#     print("It is a uppercase string")
# else:    
#     print("It is a special character")

    #ASC Code
# chr =  ord(input("Enter any one character:"))
# if chr >=65 and chr <=90:
#     print("It is a uppercase character")
# elif chr >=97 and chr <=122:
#     print("It is a lowercase character")
# elif chr >=48 and chr <=57:
#     print("It is a Digit")
# else:
#     print("It is a special character")

#membership operator
# in operator and not in operator
# name = "Help4code"
# print("z" in name)
# print("p" not in name)
# print("H" in name)

# #identity operator
# # is operator and is not operator
# math = 50
# chem = 50
# print(math is chem)
# print(math is not chem)

#for loop
#for(initialization; condition; increment/decrement)
# for i in range(5):
#     print(i)
# for j in range(2,11,2):
#         print(j)
# for k in range(10,0,-1):
#     print(k)
# for i in range(2,21,2):
#     print(i)

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):   
#     print(i*2 ," ", i * 3 ," ", i * 4," ", i * 5 ," ", i * 6 ," ", i * 7 ," ", i * 8 ," ", i * 9 ," ", i * 10 )
# print("--------------------------------------------------------------------------------------------")
# for i in range(1,11):
          
#           print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)


#WAP to accept 3 paper marks and calculate total, average and percentage and check if he/she is passed in all subjeects so print pass else print fail.

#if perecentage is greater than 65 and gender="female" then print "you are eligible for placement" else print "you are not eligible "

# a=input("Enter gender: ")
# x = int(input("Enter marks for subject 1: "))
# y = int(input("Enter marks for subject 2: "))
# z = int(input("Enter marks for subject 3: "))

# total = x + y + z
# average = total / 3
# percentage = (total / 300) * 100
# print("Total marks: ", total)
# print("Average marks: ", average)   
# print("Percentage: ", percentage) 
# if x >= 40 and y >= 40 and z >= 40:
#     print("Pass")
# else:
#     print("Fail")

# if percentage > 65 and a == "female":
#     print("You are eligible for placement")
# else:   
#     print("You are not eligible for placement")

#     # gender = input("Enter you gender M/F")
#     # IF percentage >=65 and gender == "F":
#     #     print("You are eligible for placement")   
#     # else:
#     #     print("You are not eligible for placement")   


# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(1,6) :
#     if i == 3:
#         continue
#     print(i , " " , 6-i , " ")
 #zip() we can take multiple range function in one loop
    #for i,j in zip(range(1,6),range(5,0,-1)):
    #     if i == 3 or j == 3 :
    #         continue
    #     print(i , " " , j , " ")

   
