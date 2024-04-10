books_dict = {
    1: {"author": "George Orwell", "title": "1984", "genre": "Dystopian fiction"},
    2: {"author": "Harper Lee", "title": "To kill a mockingbird", "genre": "Southern gothic"},
    3: {"author": "J.K. Rowling", "title": "Harry Potter and the sorcerer's stone", "genre": "Fantasy"}
}

def add_book(books_dict):
    author = input("Enter the author's name: ")
    title = input("Enter the book title: ")
    genre = input("Enter the genre of the book: ")

    book_id = max(books_dict.keys()) + 1
    books_dict[book_id] = {"author": author, "title": title, "genre": genre}

    return books_dict

def search_book(books_dict):
    search = input("Enter the book title or author's name: ").lower()

    for book_id, book_info in books_dict.items():
        if search in book_info['author'].lower() or search in book_info['title'].lower():
            return f"Title: {book_info['title']}, author: {book_info['author']}, genre: {book_info['genre']}"

    return "Book not found."

def choose_action():
    while True:
        action = input("Enter 'add' to add a book, 'search' to find a book, or 'exit' to quit: ").lower()

        if action == "exit":
            break
        elif action == "add":
            print(add_book(books_dict))
        elif action == "search":
            print(search_book(books_dict))
        else:
            print("Something went wrong. Try again")


choose_action()


