"""

Unordered
Cant use index
Removes duplicated elements

"""

names = {'Ram','Sam','Sandy'}

print(names) #every time elements shuffles

#access values using FOR Loop

for name in names :
    print(name)

#adding new element

names.add('Sara')

#update another set

a = {'kumar','Suersh'}

names.update(a)
print(names)
names.remove('kumar') #name which is not in a set, it will through an error, better use discard()
print(names)

names.discard('sumar')
print(names)

names.pop()  #remove random values bcos it is not indexed
print(names)

"""
union
intersect
"""

a={1,2,3,4}
b={'a','b','c','d'}

c=a.union(b)

print(c)

#how to insert it in a set itself**
#solution

a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}

c = a.intersection(b)
print(c)

a.intersection_update(b)
print(a)

"""
symmetric difference
"""
a={1,2,3,4,5}
b={5,6,7,8,9}

c=a.symmetric_difference(b)
print(c)

a.symmetric_difference_update(b)
print(a)

"""
is disjoint
"""
a={1,2,3,4,5}
b={5,6,7,8,9}

c=a.isdisjoint(b)
print(c)

c=a.issubset(b)
print(c)

c=a.issuperset(b)
print(c)