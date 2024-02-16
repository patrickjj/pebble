import json
import datetime

class Book:
    def __init__(self, title, author, start_date=None, end_date=None, rating=None):
        self.title = title
        self.author = author
        self.start_date = start_date
        self.end_date = end_date
        self.rating = rating

    def to_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "start_date": self.start_date if self.start_date else None,
            "end_date": self.end_date if self.end_date else None,
            "rating": self.rating
        }

def load_books():
    with open("books.json", "r") as f:
        books = json.load(f)
        return [Book(**book) for book in books]

def save_books(books):
    with open("books.json", "w") as f:
        json.dump([book.to_json() for book in books], f, indent=4)



def update_books():
    books = load_books()
    unfinished_books = [book for book in books if book.start_date and not book.end_date]
    if unfinished_books:
        print("You have unfinished books!")
        for book in unfinished_books:
            print(f"- {book.title} by {book.author}")
        print("Have you finished any of these books?")
        answer = input("(y/n): ").lower()
        if answer == "y":
            finished_books = []
            for book in unfinished_books:
                print(f"Enter the date you finished {book.title} by {book.author}:")
                end_date = input()
                book.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                print(f"Enter your rating for {book.title} by {book.author} (1-10):")
                rating = int(input())
                book.rating = rating
                finished_books.append(book)
            for book in finished_books:
                books.remove(book)
            books.extend(finished_books)
            save_books(books)
        else:
            print("Okay, I'll leave your books as is.")
    else:
        print("You have no unfinished books!")

    answer = input("Have you started any new books? (y/n): ").lower()
    if answer == "y":
        for i in range(1, int(input("How many new books have you started? ")) + 1):
            print(f"Book {i}")
            print("Enter the start date:")
            start_date = input()
            print("Enter the title:")
            title = input()
            print("Enter the author:")
            author = input()
            books.append(Book(title, author, start_date))
        save_books(books)
    else:
        print("Okay, no new books.")

update_books()

