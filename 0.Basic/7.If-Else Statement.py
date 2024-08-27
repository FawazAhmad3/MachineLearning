# If-Else Condition

age = int(input("Enter Your Age : "))

if age >= 1 and age < 18:
    print("You are not Eligible for ATM card")
elif age >= 18 and age <=90:
    print("You are Eligible")
else:
    print("Sorry we donot make card in this age")