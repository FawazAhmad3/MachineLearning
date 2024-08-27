f= open(r'/Users/apple/Documents/programing /python/1.Filing/data.csv','r')
ro = csv.reader(f,delimiter=',')
ld =list(ro)
for row in ld:
    print(row)