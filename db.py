import sqlite3

def get_db_connection():
    conn = sqlite3.connect('library.db')
    return conn

def fetch_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT books.book_id, books.title, authors.first_name, authors.last_name, publishers.name, genres.name, books.publication_year, books.price, books.available_copies
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    JOIN publishers ON books.publisher_id = publishers.publisher_id
    JOIN genres ON books.genre_id = genres.genre_id;
    ''')
    books = cursor.fetchall()
    conn.close()
    return books

def search_books_by_title(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT books.book_id, books.title, authors.first_name, authors.last_name, publishers.name, genres.name, books.publication_year, books.price, books.available_copies
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    JOIN publishers ON books.publisher_id = publishers.publisher_id
    JOIN genres ON books.genre_id = genres.genre_id
    WHERE books.title LIKE ?;
    ''', ('%' + title + '%',))
    books = cursor.fetchall()
    conn.close()
    return books

def search_books_by_author(author_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    print(f"Searching for author: {author_name}")  # Debugging line to track search input
    cursor.execute('''
    SELECT books.book_id, books.title, authors.first_name, authors.last_name, publishers.name, genres.name, books.publication_year, books.price, books.available_copies
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    JOIN publishers ON books.publisher_id = publishers.publisher_id
    JOIN genres ON books.genre_id = genres.genre_id
    WHERE LOWER(authors.first_name) LIKE LOWER(?) OR LOWER(authors.last_name) LIKE LOWER(?);
    ''', ('%' + author_name.lower() + '%', '%' + author_name.lower() + '%'))  # Case insensitive search
    books = cursor.fetchall()
    print(f"Found books: {books}")  # Debugging line to view found results
    conn.close()
    return books

def add_new_book(title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO books (title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', (title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies))
    conn.commit()
    conn.close()
