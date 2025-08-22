from fastapi import FastAPI

app = FastAPI(
    title="Mini Book Store"
    )
# to main book page
@app.get('/')
def root():
    return {"message": " Welcome to Mini Book Store"}

# Fake book data
books = {
    1: {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    2: {"title": "Python Tricks", "author": "Dan Bader", "genre": "Coding"},
    3: {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Coding"},
    4: {"title": "You Don't Know JS", "author": "Kyle Simpson", "genre": "Coding"},
    5: {"title": "FastAPI", "author": "Ashwin", "genre": "DBMS"},
}

# to get books based on the value
@app.get('/books/id/{book_id}')
def get_books(book_id: int):
    book =  books.get(book_id)
    if not book:
        return {"message": "Book not found"}
    return {
        "message": f"Book found {book['title']} by {book['author']}"
    }

# to get books based on author search
@app.get('/books/search')
def search_books(author: str = None):
    if author:
        results = [book for book in books.values() if book['author'].lower() == author.lower()]
        return results or {"message": "Book not found"}
    return books

# search based on the genre
@app.get('/books/search/genre')
def search_genre(genre: str=None):
    if genre:
        results = [book for book in books.values() if book['genre'].lower() == genre.lower()]
        return results or {"message": "Book not found"}
    return books
