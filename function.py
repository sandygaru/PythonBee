def welcome():
    print("Welcome Sandy")


welcome()

welcome()

"""
9 types of function
"""


# No Return Type Without Argument Funtion

def add():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    c = a + b
    print("Total : ", c)


add()


# No Return Type With Arguemnt Function

def sub(a, b):
    c = a - b
    print("Difference : ", c)


sub(25, 2)


# Return Type Without Argument Function

def mul():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    c = a * b
    return c


print(mul())


# Return Type With Arguemnt Function

def div(a, b):
    c = a / b
    return c


print(div(5, 2))


# Arbitrary Arguments Function  (*)

def class_10(*students):
    print(students)
    for user in students:
        print(user)


class_10("Ram", "Sandy", "Sara")


# Keyword Arguments Function

def message(name, age):
    print(name, " age is ", age)


message(age=25, name="Ram")


# Arbitary Keyword Arguments

def bioData(**data):
    print(data)


bioData(name="Ram Kumar", age=25, gender="Male")


# Default Parameter Function

def user(name, city="Salem"):
    print(name, " is from ", city)


user("Ram", "Coimbatore")
user("Sandy")


# Passing List as an Arguemnt

def total(marks):
    return sum(marks)


print(total([55, 64, 65, 89]))


# Recursion Function

def factorial(x):
    if (x == 1):
        return 1
    else:
        return (x * factorial(x - 1))


print(factorial(5))


#lambda function

c = lambda a:a+5
print(c(5))

c = lambda a,b : a*b

print(c(10,25))