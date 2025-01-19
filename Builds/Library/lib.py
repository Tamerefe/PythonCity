import os
import time
import sqlite3
import hashlib
from textblob import TextBlob
import tkinter as tk
import barcode
from barcode.writer import ImageWriter
from PIL import Image
from IPython.display import display

book_list = []

menu = """
                    Welcome to Dolliet's Library Factory <3

1) Donate a Book
2) Borrow a Book
3) View All Books
4) Add Book
5) Remove Book
6) Grammar Check Tool
7) Study with Stopwatch
Q) Exit

"""

# Create or connect to the database
conn = sqlite3.connect('./Builds/Library/Books/booklist.db')
c = conn.cursor()

# Create the books table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, author TEXT)''')
conn.commit()

def donate_book(book: tuple, book_list: list):
    book_list.append(book)
    print("Thank you for donating the book!")
    input("Press Enter to return to the main menu!")

def check_book(book: tuple, book_list: list) -> bool:
    return book in book_list

def borrow_book(book_title: str, book_list: list):
    borrower_name = input("Enter your name: ").strip()
    borrow_duration = input("Enter the duration you want to borrow the book for (in days): ").strip()
    c.execute("SELECT title, author FROM books WHERE title = ?", (book_title,))
    book = c.fetchone()
    if book:
        if book in book_list:
            book_list.remove(book)
        c.execute("DELETE FROM books WHERE title = ? AND author = ?", book)
        conn.commit()
        
        barcode_file = f"./Builds/Library/Books/Barcode/{book[0]}.png"
        if os.path.exists(barcode_file):
            os.remove(barcode_file)
        
        print(f"{borrower_name}, you have successfully borrowed the book for {borrow_duration} days. Happy reading!")
    else:
        print("The book you requested is not available.")
    input("Press Enter to return to the main menu!")

def list_books(book_list: list):
    c.execute("SELECT title, author FROM books")
    books = c.fetchall()
    for book in books:
        print(f"Book Title: {book[0]}       Author: {book[1]}")
    input("Press Enter to return to the main menu!")

def generate_barcode_number(title: str, author: str) -> str:
    unique_string = title + author
    hash_object = hashlib.sha256(unique_string.encode())
    return hash_object.hexdigest()[:12]  # Use the first 12 characters of the hash

def add_book(book_list: list, book: tuple):
    book_list.append(book)
    print("Book Successfully Added")
    
    barcode_number = generate_barcode_number(book[0], book[1])
    code_class = barcode.get_barcode_class('code128')
    code = code_class(barcode_number, writer=ImageWriter())
    barcode_file = code.save(f"./Builds/Library/Books/Barcode/{book[0]}")  # Include book title in file name
    
    # Save the book to the database
    c.execute("INSERT INTO books (title, author) VALUES (?, ?)", book)
    conn.commit()
    
    input("Press Enter to Return to Main Menu!")

def remove_book(book_list: list):
    title = input("Enter the title of the book to remove: ").strip()
    author = input("Enter the author of the book to remove: ").strip()
    book = (title, author)
    
    if check_book(book, book_list):
        book_list.remove(book)
        c.execute("DELETE FROM books WHERE title = ? AND author = ?", book)
        conn.commit()
        print("Book successfully removed.")
    else:
        print("The book you want to remove is not in the list.")
    
    input("Press Enter to return to the main menu!")

def correct(text):
    corrected = str(TextBlob(text).correct())
    return corrected

def study_with_stopwatch():
    stopwatch = StopWatch()
    stopwatch.mainloop()

class StopWatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Stopwatch')
        self.geometry('300x100')
        self.time = 0
        self.running = False
        self.label = tk.Label(self, text='0:00:00', font=('Helvetica', 48))
        self.label.pack()
        self.button = tk.Button(self, text='Start', command=self.start_stop)
        self.button.pack()
        self.reset_button = tk.Button(self, text='Reset', command=self.reset)
        self.reset_button.pack()

    def start_stop(self):
        self.running = not self.running
        if self.running:
            self.button.config(text='Stop')
            self.update()
        else:
            self.button.config(text='Start')

    def update(self):
        if self.running:
            self.time += 1
            minutes = self.time // 60
            seconds = self.time % 60
            hours = minutes // 60
            minutes %= 60
            self.label.config(text=f'{hours}:{minutes:02d}:{seconds:02d}')
            self.after(1000, self.update)

    def reset(self):
        self.time = 0
        self.label.config(text='0:00:00')
        self.button.config(text='Start')
        self.running = False

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
            borrow_book(title, book_list)

        elif choice == "3":
            list_books(book_list)

        elif choice == "4":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            book = (title, author)
            add_book(book_list, book)

        elif choice == "5":
            remove_book(book_list)
        
        elif choice == "6":
            text = input("Enter a sentence: ")
            corrected = correct(text)
            print(f"Corrected: {corrected}")
            input("Press Enter to return to the main menu!")

        elif choice == "7":
            study_with_stopwatch()

        elif choice == "q":
            print("Goodbye! We hope to see you again...")
            break

        else:
            print("Invalid input")
            input("Press Enter to return to the main menu!")

    conn.close()

if __name__ == '__main__':
    main()