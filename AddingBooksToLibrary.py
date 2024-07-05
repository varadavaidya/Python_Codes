Library=[]
def AddBook():

    NumberOfBooksToAdd= int(input('Number of Books you would like to add :'))
    while NumberOfBooksToAdd > 0:
        NameOfBook=input('What is the name of the book you would like to add? ')
        Author=input("Name of Author : ")
        Publication=input('publisher is : ')
        NewBook=[NameOfBook,Author,Publication]
        Library.append(NewBook)
        NumberOfBooksToAdd -= 1
    print('TheBooks in the Library are: ',Library)


AddBook()

def RemoveBook():
    MethodToRemoveBook =input('How do you want to remove" is it by Author or Book or Publisher : ')
    if MethodToRemoveBook== 'Author':
        Aut=input('name of the Author: ')
        for Book in Library:
            if Book[1]== Aut:
                Library.remove(Book)
                print(Library)
    elif MethodToRemoveBook== 'Book':
        book=input('name of the Book: ')
        for Book in Library:
            if Book[0]== book:
                Library.remove(Book)
                print(Library)
    elif MethodToRemoveBook== 'Publisher':
        pub=input('name the Publisher: ')
        for Book in Library:
            if Book[2]== pub:
                Library.remove(Book)
                print(Library)

RemoveBook()