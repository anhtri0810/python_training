import json

MENU = """ENTER
'a' - add book
's' - show books
'q' - quit
'f' - find book
'd' - delete book
YOUR CHOICE: """

books = []


def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)


def load_books():
    global books

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []


def add_book():
    title = input("Please enter the name of the book: ")
    author = input("Please enter the name of the author: ")
    year = int(input("Please enter the year when the book published: "))

    book = {
        "title": title,
        "author": author,
        "year": year
    }

    books.append(book)
    save_books()


def show_books():
    if not books:
        print("No book!!")
    else:
        for no, book in enumerate(books, start=1):
            print(f"\n============== BOOK {no} ==============")
            print(f"the title is: {book['title']}")
            print(f"the author is: {book['author']}")
            print(f"the year is: {book['year']}")


def find_book():
    n = input("Please enter the name of the book: ")

    for book in books:
        if n == book["title"]:
            print(f"The title is: {book['title']}")
            print(f"The author is: {book['author']}")
            print(f"The year is: {book['year']}")
            break
    else:
        print("We can't find the book!!")


def delete_book():
    m = input("Please enter the name of the book: ")

    for book in books:
        if m == book["title"]:
            books.remove(book)
            save_books()
            print("The book has been deleted")
            break
    else:
        print("We can't find the book")


load_books()

while True:
    choice = input(MENU).lower()

    match choice:
        case "a":
            add_book()

        case "s":
            show_books()

        case "q":
            save_books()
            print("Books saved!")
            break

        case "f":
            find_book()

        case "d":
            delete_book()

        case _:
            print("Please enter the right choice")
