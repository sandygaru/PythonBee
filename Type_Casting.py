a=10.0

print(a)

print(type(a))

b= int(a)   #converted through constructor

print(b)

print(type(b))

'''
<class 'float'>

all datatype's are class here, inorder to typecast, we need to use it own class constructor.
'''


"""IMPORTANT TO NOTE

a = int(input("enter the val of a : "))  #casting
b = int(input("enter the val of b : "))

c= a*b

print("enter " + c)

Traceback (most recent call last):
  File C:Users\saisa\PycharmProjects\PythonBee\Type_Casting.py, line 37, in <module>
    print("enter" + c)
TypeError: can only concatenate str (not int) to str


Use below, give comma in the print command if we cast the input command

print("enter"  , c)
"""

a = (input("enter the val of a : "))  #casting
b = (input("enter the val of b : "))

c= a+b

print("enter "+ c)