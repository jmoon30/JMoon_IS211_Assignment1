# assignment1_part2.py

class Book:

    """
    Constructor of the Book class

    :param author: the name of the author
    :param title: the title of the book
    """

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        return f"{self.title}, written by {self.author}"


if __name__ == "__main__":
    book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    print(book1.display())
    print(book2.display())

