# Append the data in the existing file 

import csv

f = open('/Users/apple/Documents/programing /python/1.Filing/1.3append.csv', 'a')

wo = csv.writer(f, delimiter=',')

n = int (input('Enter Number of students: '))

lr = []

for i in range(n):
    rn = int(input("Enter Roll number: "))
    n = (input("Enter Name: "))
    a = int(input("Enter Age: "))   
    wo.writerow([rn,n,a])
    

r= open(r'/Users/apple/Documents/programing /python/1.Filing/1.3append.csv','r')
ro = csv.reader(r,delimiter=',')
ld =list(ro)
for row in ld:
    print(row)

f.close()