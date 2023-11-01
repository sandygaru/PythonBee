"""

Nested IF Statement

3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100          A
    80-89           B
    70-79           C
    else            D

"""

m1 = int(input("Enter Mark - 1 : "))
m2 = int(input("Enter Mark - 1 : "))
m3 = int(input("Enter Mark - 1 : "))

total = m1 + m2 + m3
print("Total : ", total)
average = total / 3.0
print("Average : ", average)
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result : Pass")
    if 90 <= average <= 100:
        print("Grade : A")
    elif 80 <= average <= 89:
        print("Grade : B")
    elif 70 <= average <= 79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result : Fail")
    print("Grade : Nil")
