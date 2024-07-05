#NameOfTheUser=input('what is your name?')
'''
if NameOfTheUser == 'Varada':
    pswd = 'Gayatri565@'
    print("you're the true owner and the password is : ", pswd)
else:print("You are not the true owner")

'''


List=['mysuru','Bangaluru','Sringeri']

def PlacesVisited():
    k=input('type the place you think you visited : ')
    if k in List:
        print("you have visited the place")
    else:print("youvent visited")

PlacesVisited()