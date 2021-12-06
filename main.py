from tkinter import *

lib = {}


class HomeLib:
    def __init__(self):
        self.__name = 1
        self.__author = 2

    def set_name(self, name):
        self.__name = name

    def set_author(self, author):
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def read(self):
        self.set_name(name_of_book.get())
        self.set_author(author_of_book.get())
        lib.update([self.full_book()])

    def full_book(self):
        return self.__name, self.__author

    def find_by_name(self):
        try:
            return lib.get(name_of_book.get())
        except:
            return "введіть іншу назву", self.find_by_name()

    def add_book(self):
        lib.update([self.full_book()])
        return lib

    def delete_book(self):
        try:
            lib.pop(name_of_book.get())
            return lib
        except:
            print("Такої книги немає")

    def print_all_lib(self):
        return lib


book = HomeLib()


def read_book():
    return book.read()


def check_book():
    list_of_books.insert(END, book.print_all_lib())


def add_book():
    return book.add_book()


def find_book():
    list_of_books.insert(END, book.find_by_name())


def delete_book():
    return book.delete_book()


root = Tk()
root.title('Домашня бібліотека')
name_of_book = Entry()
name_of_book.pack()
author_of_book = Entry()
author_of_book.pack()
read_book_to_lib = Button(text="Зчитати данні з полів", command=read_book)
read_book_to_lib.pack()

check_books_in_lib = Button(text="Показати книги в бібліотеці", command=check_book)
check_books_in_lib.pack()

add_book_to_lib = Button(text="Додати книгу до бібліотеки", command=add_book)
add_book_to_lib.pack()

find_book_in_lib = Button(text="Знайти книгу за назвою", command=find_book)
find_book_in_lib.pack()

delete_book_in_lib = Button(text="Видалити книгу з бібліотеки", command=delete_book)
delete_book_in_lib.pack()

list_of_books = Listbox()
list_of_books.pack()


root.mainloop()