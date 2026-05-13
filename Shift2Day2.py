#Tuple
#Difference between List and Tuple
# mytuple = ("anjali","Aditya","isha","Nikita",77,89.30,"Athrav","Sanchit","Ankit","Ayush")
# print(mytuple)
# print(type(mytuple))

#mytuple[0] = "Lokesh"#tuple is immutable

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)


# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)

# l=[1,2,3]
# init_tuple =('Python',)*(l.__len__()-l[::-1][0])
# print(init_tuple)

# init_tuple = ('Python')*3
# print(type(init_tuple))

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),)*7
# print(init_tuple)
# print(len(init_tuple[3:8]))

#Dictionary
# mydict =  {
#     101: "Anjali",
#     102: "Aditya",
#     "103": "Isha",
#      "104": "Nikita",
#     101: "Athrav",
#    104: "Sanchit",
# }
# print(mydict)

# a = mydict[102]
# print(a)    

# mydict[102]="adu"
# print(mydict)

# for x in mydict:
#     print(x)

# for x in mydict.values():
#  print(x)

#  for x,y in mydict.items():
#   print(x,y)

#   mydict["mobile_no"]=4646463738
#   print(mydict)

# mydict.pop(101)
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])#key error, no 2 values can't store

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum=0
# for k in arr:
#     sum +=arr[k]
#     print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#     print (sum)

# my_dict= {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates ={}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] =  box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print (dict[_])

# rec ={"Name" : "Python", "Age" : "20"}
# r = rec.copy()
# print(id(r) == id(rec)) #id gives address of id variable

# rec = {"Name" : "Python", "Age":"20","Addr":"NJ","Country":"USA"}
# id1 = id(rec)
# print(id1)
# del rec 
# rec = {"Name" : "Python", "Age":"20","Addr":"NJ","Country":"USA"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)

# rec={"A":50,"B":30,"C":70}
# for i in sorted(rec.values()):
#     print(i)
    
# rec = {"A": 50, "B": 30, "C": 70}

# # Find the key with the maximum value
# max_key = max(rec, key=rec.get)

# print(max_key)   # Output: C

# rec = {"X": 20, "Y": 10, "Z": 30}

# min_key = min(rec, key=rec.get)

# print(min_key)   # Output: Y
# data = [1, 2, 2, 3, 4, 3, 5]

# freq = {}
# for item in data:
#     # Convert to string if you want string keys
#     key = str(item)
#     if key in freq:
#         freq[key] += 1
#     else:
#         freq[key] = 1

# print(freq)

# num = 123
# a =num % 10
# num =num //10
# b = num % 10
# c = num // 10
# rev = a*100+b*10+c*1
# print(rev)

# num=123456
# a=num%10
# num=num//10
# b=num%10
# num=num//10
# c=num%10
# num=num//10
# d=num%10
# num=num//10
# e=num%10
# num=num//10
# f=num%10
# num=num//10
# rev=a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)

Amount = int(input("Please Enter Amount for Withdraw :"))
print (" 100 notes= ",Amount//100)
print (" 50 notes= ",(Amount%100)//50)
print (" 20 notes= ", ((Amount%100)%50)//20)
print (" 10 notes= ",(((Amount % 100)%50)%20)//10)
print(" 5 notes= ",((((Amount %100)%50)%20)%10)//5)
print(" 2 coin= ",(((((Amount %100)%50)%20)%10)%5)//2)
print("1 coin= ", ((((((Amount %100)%50)%20)%10)%5)%2)//1)










