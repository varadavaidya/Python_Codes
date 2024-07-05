import csv
Address= r'C:\Users\varad\OneDrive\Desktop\cc.csv'

with open(Address) as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    alpha=[]
    num=[]

    for row in readcsv:
        alpha.append(row)

print(alpha)