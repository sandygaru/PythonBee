"""

key value pair
keys shouldnt be duplicate

"""
user = {
    "name": "Sandy",
    "age": 25,
    "isMarried": False
}

print(user)

print(type(user))

print(user["name"])

print(user.get('age'))

print(user.keys())

print(user.values())

print(user.items())

for x in user:
    print(x)
    print(x, "   ", user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x, y in user.items():
    print(x, y)

if "age" in user:
    print("present")

if "mobile" in user:
    print("present")
else:
    print("absent")

#############

user.update({"gender": "male"})
print(user)

user["age"] = 35

print(user)

user.pop("age")
print(user)

user.clear()

print(user)
# del user

user = {

    "user1": {
        "name": "Sandy",
        "age": 25,
        "isMarried": False
    },
    "user2": {
        "name": "Kaaru",
        "age": 25,
        "isMarried": False
    }
}

print(user)

print(user['user2']['name'])