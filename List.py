"""

List

Sequence Type
Mutable
Handles Hetergeneous types
Nested List Possible

"""

a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0] = 100
print(a)

"""
Slicing
"""
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("***********")

b = [1, True, 'Ram', 2.5]

print(a)
print(a[0], "type is ", type(a[0]))
print(a[1], "type is ", type(a[0]))
print(a[2], "type is ", type(a[0]))
print(a[3], "type is ", type(a[0]))

print("***********")

a = [1, 2, 3, [1, True, 'Ram', 2.5]]

print(a[3][2])

a.clear()

print(a)

a = b.copy()

print(a)

"""
counting elements in a list
"""
a = [1, 2, 3, 4, 5, 1, 5, 2, 5]

print(a.count(5))

#finding index

print(a.index(3)) # only for first occurence

print(len(a))

print(max(a))
print(min(a))

#POP

print(a)

a.pop(0)  #removes index based

print(a)

a.remove(5) #removes first occurences of the value given (value based)

print(a)

print("*****************")

names = ["Ram"]

names.append("sam")

print(names)

names_female = ["Sara", "Caro"]

names.extend(names_female)   #adding a list in a list

print(names)

names.insert(0,"Santhosh")   #adding based on index

print(names)

print(list(range(5)))

print(list("SANTHOSH SANDY"))

a = [10,50,100,25,85]

a.sort()

print(a)

a.sort(reverse=True)
print(a)


a=["Orange","Aple","Paaya"]

a.sort()
print(a)
a.sort(key=len)
print(a)