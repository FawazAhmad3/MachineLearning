# Loops in Python
'''
1. While Loop
2. For Loop
3. Nested Loop
'''

'''
# While Loop

i = 0
while i <= 10:
    print(i)
    i = i+1

# Input From User in While Loop

j = int(input("Enter a Number : "))
while j <= 10:
    print(j)
    j = j+2
'''

# For Loop
'''
a = 0
for a in range (0,6) :
    print(a)

# Input From User in For Loop

num = int(input("Enter a Number for table : "))
for b in range(1 , 11):
    print(num*b)
    b = b+1
'''

# Nested loop

color = ["White", "Black", "yellow"]
car = ["Yaris", "Civic", "Prado"]
for x in color:
    for y in car:
        print(x , y)