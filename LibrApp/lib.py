import os

book_list = []

menu = """
                    Welcome to Dolliet's Library Factory <3

1) Donate a Book
2) Borrow a Book
3) View All Books
Q) Exit

"""

def donate_book(book: tuple, book_list: list):
    book_list.append(book)
    print("Thank you for donating the book!")
    input("Press Enter to return to the main menu!")

def check_book(book: tuple, book_list: list) -> bool:
    return book in book_list

def borrow_book(book: tuple, book_list: list):
    if check_book(book, book_list):
        book_list.remove(book)
        print("You have successfully borrowed the book. Happy reading!")
    else:
        print("The book you requested is not available.")
    input("Press Enter to return to the main menu!")

def list_books(book_list: list):
    for book in book_list:
        print(f"Book Title: {book[0]}       Author: {book[1]}")
    input("Press Enter to return to the main menu!")

def main():
    while True:
        os.system("cls")
        print(menu)

        choice = input("Enter the operation number: ").strip().lower()

        if choice == "1":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            book = (title, author)
            donate_book(book, book_list)

        elif choice == "2":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            book = (title, author)
            borrow_book(book, book_list)

        elif choice == "3":
            list_books(book_list)

        elif choice == "q":
            print("Goodbye! We hope to see you again...")
            break

        else:
            print("Invalid input")
            input("Press Enter to return to the main menu!")

if __name__ == "__main__":
    main()
