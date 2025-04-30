class Library:
    books =[]
    def checkActivity():
        Input1 = input("Do you wish to add a new book. Type 1 for Yes or 2 for No")
        while Input1 == "1":
        #if Input1 == "1" :
            Library.addBook()
            Library.printBook()
            Input1 = input("Do you wish to add a another book. Type 1 for Yes or 2 for No")
           # if Input1 == "1":
                # Library.addBook()
                # Library.printBook()
            #else:
               # Library.printBook()
        else:
            Input2 = input("Do you wish to view the library? Type 1 for Yes or 2 for No")
            if Input2 == "1":
                Library.printBook()
            else:
                exit
    def addBook():
        name = input("Enter Book Name : ")
        author = input("Enter Author Name : ")
        year = input("Enter Published Year : ")
        BookDetails ={
            "Bname":name,
            "BAuthor":author,
            "Byear": year
        }
        Library.books.append(BookDetails)
        print("Book added sucessfully")
    def printBook():
        print("You added",Library.books)

Library.checkActivity()