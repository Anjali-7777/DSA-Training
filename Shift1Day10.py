# import re
# count = 0
# pattern = re.compile("marks")

# matcher = pattern.finditer("Anjali score 29 marks in AI,Isha score 22 marks and marks are given by teacher.")
# for i in matcher:
#     count += 1
#     print(i.start(),".....",i.end(),".....",i.group())
# print("The number of occurences: ",count)

# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count += 1
#     print(i.start(),".....",i.end(),".....",i.group())
# print("The number of occurences: ",count)

# import re
# obj = input("Enter any character")
# objmatch = re.finditer(obj,"a7b @k9z")

# for match in objmatch:
    
#  print(match.start(),".....",match.end(),".....",match.group())

# import re
# a = input("Enter string to perform match operation:")
# match = re.match(a,"python is very important language")
# print(match)

# if match!= None:
#   print("match found at beginning level")
#   print(match.start()," ",match.end())

# else:
#     print("there is no matching at beginning level")



# import re
# a = input("Enter string to perform match operation:")
# match = re.fullmatch(a,"pythonisvery")
# print(match)

# if match!= None:
#   print("match found ")
#   print(match.start()," ",match.end())

# else:
#     print("Full match not found")


# import re
# s = input("Enter Mail id:")
# match = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# print(match)

# if match!= None:
#   print("Valid E-Mail Id")


# else:
#     print("Invalid E-Mail Id")

# import re
# s = input("Enter Mail id: ")
# match = re.fullmatch(r"\w[a-zA-Z0-9_.]*@rbunagpur\.in", s)
# if match:
#     print("Valid E-Mail Id")
# else:
#     print("Invalid E-Mail Id")


# import re
# s = input("Enter Mobile Number: ")
# match = re.fullmatch(r"\d{10}", s)
# if match:
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")


# import re
# a = input("Enter string to perform match operation:")
# match = re.search(a,"python sss dynamic lannn")



# if match!= None:
#   print("match found ")
#   print(match.start()," ",match.end()," ",match.group())
#   print(match)

# else:
#     print("There is no matching anywhere")

# import re
# match =  re.findall('[0-9a-z]',"abch3hdh5bk7hzZWUnbsgOiNH%*7W")
# print(match)

# import re
# match =  re.findall('[0-9a-z]',"abch3hdh5bk7hzZWUnbsgOiNH%*7W")
# print(match)

# import re
# match =  re.findall('[A-Z]',"abch3hdh5bk7hzZWUnbsgOiNH%*7W")
# print(match)

# import re
# obj = re.sub('[a-z]','*','2345 ABCD habc deff')
# print(obj)

# import re
# obj = re.subn('[0-7]','*','ab356tggedeijmkidy89jnd')
# print(obj)
# print("the string is=", obj[0])
# print("the number of replacement is=",obj[1])


# import re
# f1=open("newfile.txt","r")
# f2=open("output.txt","w")
# a = input("enter string to perform match operation ")
# objmatch=re.finditer(a,f1.read())
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())
#     f2.write(str(match.start())+"..."+str(match.end())+"..."+str(match.group()))

import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exists:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)

 




