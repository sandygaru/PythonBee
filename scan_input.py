# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 06:22:14 2023

@author: saisa
"""

#input statement  -- considers only string

"""
name = input("Please enter your name : ")
print(type(name)) #always string
print(name)
"""

"""
a = int(input("enter the val of a : "))  #casting
b = int(input("enter the val of b : "))

c= a*b

print(c)

"""

"""
a = float(input("enter the val of a : "))  #casting
b = float(input("enter the val of b : "))

c= a*b

print(c)
"""

#fetch multiple vals from user

#name1,name2,name3 = input("Enter 3 names").split()  #default split by space

"""
name1,name2,name3 = input("Enter 3 names").split(',') #seperated by comma

print("name1 ",name1)
print("name2 ",name2)
print("name3 ",name3)
"""

#multiline string

abc="""
sknaskc slcnknalscnkn slacjknlasc 
sllcnnkasnc slacnasalc 
cnaskc  kscnskac 
 cakcnnsa skcjas c
  caskcnas
"""

print(abc)

print()
#passing multiline string to a list
para_list=[]

print("enter a para")

while True:
    line=input()
    if line:
        para_list.append(line)
    else:
        break

print(para_list)
print()
output='\n'.join(para_list)

print(output)
print()

#passing list to a multiline string

para = ["ska","asia","aska"]

print(','.join(para))

print()


