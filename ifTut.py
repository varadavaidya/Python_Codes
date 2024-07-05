#create txt file

TxtFile=open('CreatedTXTFile.txt','w')
#write into that txt file

TxtFile.write('Hi there!')

#append to it a new line saying my name is varada...you still use "write" operation not append

TxtFile=open('CreatedTXTFile.txt','a')

TxtFile.write("\nMy name is Varada.")


#read the file

TxtFile=open('CreatedTXTFile.txt','r')
print(TxtFile.read())






