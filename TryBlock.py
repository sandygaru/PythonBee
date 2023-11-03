try:
    a = 10 / 0
except Exception as e:
    print(e)

print("****************")


try:
    a = 10 / 2
except Exception as e:
    print(e)
else:
    print("A value : ", a)

print("****************")

try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value : ", a)
finally:
    print("Final Block")
    print("****************")
    """
    Types of Exception
    """
    print(dir(locals()['__builtins__']))

    print(len(dir(locals()['__builtins__'])))

    print("****************")

    #name error exception

try:
    print(b)
except NameError as e:
    print("b is not defined")


