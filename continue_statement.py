"""

Continue statement

print odd numbers only 1-20
"""

i = 1
n = 20

while i <= n:
    if i % 2 == 0:
        i = i + 1
        continue
    print(i)
    i += 1
