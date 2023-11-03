"""

identify to compare 2 objects equal or not

is
is not
"""

a = [1, 2]
b = [1, 2]

c = a
print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
print(a == b)
print(a == c)

print(a is not b)
