"""

ElIf Statement

0       No Fine
1-5     0.5
5-10    1
10-30   5
>30     Membership Cancel

"""

days = int(input("Enter a number : "))

if days == 0:
    print(" Good No Fine !!!")
elif 1 <= days <= 5:
    print(" Fine Amount : ", days*0.5)
elif 5 < days <= 10:
    print(" Fine Amount : ", days*1)
elif 10 < days <= 30:
    print(" Fine Amount : ", days*5)
else:
    print(" Membership Cancel !!!")

