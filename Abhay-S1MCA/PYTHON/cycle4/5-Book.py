class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("\n*********************\nBook Details\n*********************")
        print("Publisher Name : ",self.name)


class Book(Publisher):
    def __init__(self, title, author, name):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title : ",self.title)
        print("Author : ",self.author)


class Python(Book):
    def __init__(self, name, title, author, prize, pages):
        super().__init__(title, author, name)
        self.prize = prize
        self.pages = pages

    def display(self):
        super().display()
        print("Price : ",self.prize)
        print("No of Pages : ",self.pages)

name = input("Enter The publisher : ")
title = input("Enter The Book Title : ")
author = input("Author Name : ")
prize = int(input("Enter Price : "))
page = int(input("Enter No.of Pages : "))

ob = Python(name, title, author, prize, page)
ob.display()
