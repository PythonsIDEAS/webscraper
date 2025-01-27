import sqlite3

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row  # Enables fetching rows as dictionaries
    return conn

# Initialize the database and create tables
def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create Authors Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER,
        nationality TEXT,
        biography TEXT,
        created_at TEXT DEFAULT (datetime('now', 'localtime'))
    );
    ''')

    # Create Publishers Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT,
        founded_year INTEGER,
        website TEXT
    );
    ''')

    # Create Genres Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres (
        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );
    ''')

    # Create Books Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        publisher_id INTEGER,
        genre_id INTEGER,
        publication_year INTEGER,
        isbn TEXT,
        price REAL,
        pages INTEGER,
        available_copies INTEGER DEFAULT 0,
        created_at TEXT DEFAULT (datetime('now', 'localtime')),
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id),
        FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
    );
    ''')

    conn.commit()
    conn.close()

# Fetch all books
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

# Search books by title
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

# Search books by author
def search_books_by_author(author_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Clean the input by trimming spaces
    clean_author_name = author_name.strip()

    query = '''
    SELECT books.book_id, books.title, authors.first_name, authors.last_name, publishers.name, genres.name, books.publication_year, books.price, books.available_copies
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    JOIN publishers ON books.publisher_id = publishers.publisher_id
    JOIN genres ON books.genre_id = genres.genre_id
    WHERE authors.first_name LIKE ? OR authors.last_name LIKE ?;
    '''

    cursor.execute(query, ('%' + clean_author_name + '%', '%' + clean_author_name + '%'))
    books = cursor.fetchall()
    conn.close()
    return books

# Add a new book
def add_new_book(title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO books (title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', (title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies))
    conn.commit()
    conn.close()

# Update author details
def update_author(author_id, first_name, last_name, birth_year, nationality, biography):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE authors
    SET first_name = ?, last_name = ?, birth_year = ?, nationality = ?, biography = ?
    WHERE author_id = ?;
    ''', (first_name, last_name, birth_year, nationality, biography, author_id))
    conn.commit()
    conn.close()

# Update book details
def update_book(book_id, title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE books
    SET title = ?, author_id = ?, publisher_id = ?, genre_id = ?, publication_year = ?, isbn = ?, price = ?, pages = ?, available_copies = ?
    WHERE book_id = ?;
    ''', (title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies, book_id))
    conn.commit()
    conn.close()

# Update publisher details
def update_publisher(publisher_id, name, country, founded_year, website):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE publishers
    SET name = ?, country = ?, founded_year = ?, website = ?
    WHERE publisher_id = ?;
    ''', (name, country, founded_year, website, publisher_id))
    conn.commit()
    conn.close()

# Update genre details
def update_genre(genre_id, name, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE genres
    SET name = ?, description = ?
    WHERE genre_id = ?;
    ''', (name, description, genre_id))
    conn.commit()
    conn.close()

# Initialize the database if this script is run directly
if __name__ == "__main__":
    initialize_db()


