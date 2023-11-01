"""

Sequence Type
Immutable

"""

a = (1, 2.5, True, "Ram")
print(a)
print(type(a))

print(a[1])

print(a[-1])

print(a[0:2])

b = list(a)
print(b)
b.append("Sandy")

a = tuple(b)
print(a)

print("***********************")
for i in a:
    print(i)

if "Ram" in a:
    print("Found")
else:
    print("Not FOund")


a = (1)

print(type(a))  #still itsan int not an tuple

a = (1,)

print(type(a))  #adding comma it treated as tuple

#del a

print(a)

a= (1,2,7,4)

b= (5,6,7,8)

c = a + b

print(c)

print(c.count(7))

"""
Nested TUples
"""

a= (1,2,7,4)

b= (5,6,7,8)

c = (a, b)

print(c)
print(c[1][2])
x = ('San',) * 10

print(x)

a = (9,5,1,7,5,3)

print(max(a))
print(min(a))