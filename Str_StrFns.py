#String and String Functions

s = ("sandy hello hi")

print(s)

print(type(s))

print(s.upper())

print(s.lower())

print(s.capitalize())

print(s.title())

print(s.count("l"))

print(s.endswith("llo"))

print(s.find("h"))

print(s.find("h",7))

print(s.replace("h","-99"))

print(s.islower())

print(s.isupper())

print(s.isspace())

print(s)

print(s.isalnum())
print("****************1")
sc="he\nis\ngood"

print(sc)

print(sc.splitlines())

print(sc.splitlines(True))
print("****************2")
a= "santhosh_sandy_kaarunyan"
print(a.split("_"))

b="    asksj      "
print(len(b))
print(len(b.strip()))
print(len(b.lstrip()))
print(len(b.rstrip()))

c="12-03-2023"

print(c.partition("-"))