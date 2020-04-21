

import csv

myfile1 = open("cityhash.csv","r",encoding='utf-8')
myfile2 = open("addColumn.csv","w",encoding='utf-8')
counter = 0
for i in myfile1:
    myfile2.write(',' + i)
    break
for i in myfile1:
    myfile2.write(str(counter)+',' + i)
    counter = counter + 1
myfile1.close()
myfile2.close()