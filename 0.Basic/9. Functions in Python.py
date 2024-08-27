# Functions in Python

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("The Add is : " ,add(6,7))
print("The Mul is : " ,mul(8,9))

def admit_card(name,age,ph_num):
    print("Name is {0}, Age is {1}, Ph_num is {2}".format (name,age,ph_num))

admit_card("fawaz","19","1234567890")

# Input from user
print("  ")
print("Input From User : ")
print("  ")

a=str(input("Enter Your name : "))
b=int(input("Enter Your age : "))
c=int(input("Enter Your Phone Number : "))

admit_card(a,b,c)