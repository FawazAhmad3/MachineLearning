# Create the new file and Write the data in the File 

import csv
f= open(r'/Users/apple/Documents/programing /python/1.Filing/1.2write.csv','w')
wo = csv.writer(f,delimiter=',')

data = [[1,2,3,4],
        [11,12,13,14],
        [21,22,23,25]]

wo.writerows(data)

f.close()