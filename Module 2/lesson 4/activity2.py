class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has beem updated. you can take the book now")
        else:
            print(f"Book is already being usedby {self.lendDict[book]}")
    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
if __name__ == '__main__':

    books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name}library. Enter your choice to continue")
        print("1. Display Books")
        print("2. lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
                
        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            books.lendbook(user, book)
                
        elif user_choice == 3:
            book = input ("Enter the name of the book you want to add:")
            books.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continues")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 =="c":
                continue