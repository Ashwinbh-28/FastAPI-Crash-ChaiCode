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
    2: {"title": "Python Tricks", "author": "Dan Bader"},
    3: {"title": "Clean Code", "author": "Robert C. Martin"},
    4: {"title": "You Don't Know JS", "author": "Kyle Simpson"},
    5: {"title": "FastAPI", "author": "Ashwin"},
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
        results = [book for book in books.values() if book['author'] == author]
        return results or {"message": "Book not found"}
    return books
