"""

&   AND
|   OR
^   XOR    --> if both binary is same,0 else 1
~   NOT
<<  Zero fill left shift
>>  Signed right shift

"""

a=10  # 1010
b=11  # 1011

print(a & b)  #1010  = 10

print(a | b)  #1011  = 11

print(a ^ b) #0001  = 1

print(~a) #a+1 --> -a ==> 10+1 = 11 --> -11

print(a<<2) # left shift and manipulate with 8 bits  0000 1010 ==> 00 1010  00 ==> 0010 1000

print(a>>2) # right shift and manipulate with 8 bits  0000 1010 ==> 0000 0010