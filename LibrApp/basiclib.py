book_list = list()

menu = """

1) Add Book
2) Remove Book
3) Show Books
Q) Quit

"""

def add_book(list, book):
    list += [book]
    print("Book Successfully Added")
    input("Press Enter to Return to Main Menu!")

def remove_book():
    pass

def show_books(list):
    for book in list:
        print("Book Name >>>>>>>> {} ".format(book))
    input("Press Enter to Return to Main Menu!")

def quit_program():
    quit()

while True:
    print(menu)

    choice = input("Your Choice:")

    if choice == "1":
        book_name = input("Book Name")
        add_book(book_list, book_name)
    elif choice == "2":
        remove_book()
    elif choice == "3":
        show_books(book_list)
    elif choice == "Q" or choice == "q":
        quit_program()
    else:
        print("Invalid Choice")
        input("Press Enter to Return to Main Menu!")