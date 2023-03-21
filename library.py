class Library_item:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        available = "available"
        occupied = "occupied"
        if self.status == available:
            print(f"it's {available} for booking")
        if self.status == occupied:
            print(f"it's {occupied} for booking")
        else:
            return False

class Book(Library_item):
    def __init__(self, ISBN, authors, title, subject, status):
        self.ISBN = ISBN
        self.authors = authors
        super().__init__(title, subject, status)

    def booking(self):
        super().booking()


class Magazine(Library_item):
    def __init__(self, journalName, volume, status):
        self.journalName = journalName
        self.volume = volume
        self.status = status

    def booking(self):
        super().booking()

class CD(Library_item):
    def __init__(self, title, status):
        self.title = title
        self.status = status
    def __str__(self):
        return "u can't book this"
library = Library_item("ragac", "ragacis", "available")
# print(library.booking())
book = Book("ragac", "vigac", "ragac", "ragacis", "occupied")
# print(book.booking())
magazine = Magazine("name", "vol1", "available")
#print(magazine.booking())
cd = CD("cd", "available")
print(cd)
