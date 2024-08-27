# Rules for making variable in python
'''
These are invalid things
1. Do not use Space while making variable (my name = "Fawaz";)
2. Do not use Special Characters making variable (n@me = "Fawaz";)
3. Do not use number as a first character of variable (8name = "Fawaz";)

Valid
1. my_name = Fawaz;
2. name = Fawaz;
3. name8 = Fawaz;
'''

# Data Types in Python

'''
1. Numeric (int, float, complex)
2. Sequence type (String, List, Tuple)
3. Set
4. Boolean
5. Dictionary
'''
# Numeric datatype

a = 6;
b = 10.5;
c = 6j;

print ("a = ",a)
print ("b = ",b)
print ("c = ",c)

# To show the types of values

print("The type of variable a is ",type(a))
print("The type of variable b is ",type(b))
print("The type of variable c is ",type(c))

# Sequencetype datatype

a = "Islamabad";
b =("Multan", "Karachi", "Lahore") ;
c = ["Pakistan", "India", "China"];

print ("a = ",a)
print ("b = ",b)
print ("c = ",c)

# To show the types of values

print("The type of variable a is ",type(a))
print("The type of variable b is ",type(b))
print("The type of variable c is ",type(c))

# Boolean

x = True
y = False

print("x = ",x)
print("y = ",y)

# To show the types of values

print("The type of variable x is ",type(x))
print("The type of variable y is ",type(y))

# Set

a = {"Pakistan", "India","Nepal"}

print("a = ",a)

# To show the types of values

print("The type of variable a is ",type(a))

# Dictionary datatype

print("Car Details:")

dict = {'Brand':'Honda','Color':'White','Model':'2019'}

print("Car Brand : ", dict['Brand'])
print("Car Color : ", dict['Color'])
print("Car Model : ", dict['Model'])

print("Student Info:")

dict = {'Name':'Fawaz', 'Age':'19'}

print("Name of Student is :", dict['Name'] )
print("Age of Student is : ", dict['Age'] )