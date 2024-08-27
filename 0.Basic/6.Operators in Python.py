# Operators in Python
'''
1) Arithmetic operator (+,-,*,/,%,//,**)
2) Assignment  operator (+=, -=, *=, /=, **=, =)
3) Comparison operator (==, >, <, <=, >=, !=)
4) Logical operator (and , or, not)
5) Bitwise operator (^, |, & , ~, <<, >> )
6) Membership operators (in, not in)
7) Identity operators (is, is not)
'''
# Arithmetic operator (+,-,*,/,%,//,**)

x = 6;
y = 5;

print("The Addition is : ", x + y)
print("The Subtraction is : ", x - y)
print("The Multiplication is : ", x * y)
print("The Division is : ", x / y)
print("The Modulus is : ", x % y)
print("The Floor Division is : ", x // y)
print("The Exponent is : ", x ** y)

# Assignment  operator (+= , -= , *= , /= , **= , =)
'''
x += 3 # x= x+3
print("The x+=3 is : ", x)
y -= 3 # y= y-3
print("The y-=3 is : ", y)
x *= 3 # x= x*3
print("The x*=3 is : ", x)
y /= 3 # y= y/3
print("The y/=3 is : ", y)
x **= 3 # x= x**3
print("The x**=3 is : ", x)
y = 3 # y=3
print("The y=3 is : ", y)
'''

# Comparison operator (==, >, <, <=, >=, !=)

print("Comparison ==", x == y)
print("Comparison >", x > y)
print("Comparison <", x < y)
print("Comparison <=", x <= y)
print("Comparison >=", x >= y)
print("Comparison !=", x != y)

# Logical operator (and , or, not)

print(x==6 and y==5) # T . T = T
print(x==7 or y==5)  # F . T = T
print(not(x==7 and y==6))  # F . F =T

# Bitwise operator (^, |, & , ~, <<, >> )

# It use Binary of number and then add them
# e.f binary of 2 is 0010 and 3 is 0011 and then it perform operation and then again convert binary ans to number

print("Bitwise for XOR ^ is ", x ^ y) 
print("Bitwise for OR | is ", x | y)
print("Bitwise for AND & is ", x & y)
print("Bitwise for NOT ~ is ", ~x)
print("Bitwise for Left Shift << is ", x << 2)
# 6*2=12 , 12*2=24 
# if we use x << 3
# 6*3=18 , 18*3=54  , 54*3=162 
print("Bitwise for Right Shift >> is ", x >> 2)
# 6/2=3 , 3/2=1
# if we use x >> 3
# 6/3=2 , 2/3=0  , 0*3=0 

# Membership operators (in, not in)
print()
print("Membership operators")

a = ["India" , "Pakistan"]
print("India" in a)

a = ["India" , "Pakistan"]
print("Nepal" in a)

a = ["India" , "Pakistan"]
print("India" not in a)

a = ["India" , "Pakistan"]
print("Nepal" not in a)

# Identity operators (is, is not)
print("")
b = ("Srilanka", "Afghanistan", "Iran")
c = ("USA", "UK", "Canada")
d = b

print(b is c)
print(b is d)

print(b is not c)
print(b is not d)