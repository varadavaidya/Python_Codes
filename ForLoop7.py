#to create lists of odd and even numbers between 1-100
x=range(1,101)
odd=[]
even=[]
for i in x:
    if (i % 2 == 0) & (i <= 50):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

print(len(even))
print(len(odd))

# Cal length of the even & odd list
length=0
for k in even:
    length+=1


print(length)