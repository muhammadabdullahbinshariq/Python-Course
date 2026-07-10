import sqlite3
import pandas as pd

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS BOOKS;
DROP TABLE IF EXISTS MEMBER;
DROP TABLE IF EXISTS BOOK_LOAN;
                     
CREATE TABLE BOOKS (
    BOOK_ID  VARCHAR(10),
    BOOK_TITLE TEXT,
    AUTHOR TEXT,
    GENRE TEXT,
    PAGES INTEGER,
    COPIES INTEGER,
    AVAILABLE INTEGER
);        
                     
CREATE TABLE MEMBER (
    MEMBER_ID TEXT,
    MEMBER_NAME TEXT,
    BOOK TEXT,
    BORROW_DATE TEXT,
    RETURN_DATE TEXT
);
                     
CREATE TABLE BOOK_LOAN (
    LOAN_ID TEXT,
    MEMBER_ID TEXT,
    BOOK_ID TEXT,
    DAYS INTEGER,
    TOTAL_FEE INTEGER
);
                     
INSERT INTO BOOKS (BOOK_ID, BOOK_TITLE, AUTHOR, GENRE, PAGES, COPIES, AVAILABLE) VALUES
("B001", "THE GREAT GATSBY", "F. SCOTT FITZGERALD", "FICTION", 180, 5, 3),
("B002", "TO KILL A MOCKINGBIRD", "HARPER LEE", "CLASSIC", 281, 4, 4),
("B003", "1984", "GEORGE ORWELL", "DYSTOPIAN", 328, 6, 2),
("B004", "A BRIEF HISTORY OF TIME", "STEPHEN HAWKING", "SCIENCE", 212, 3, 3),
("B005", "THE HOBBIT", "J.R.R. TOLKIEN", "FANTASY", 310, 8, 7),
("B006", "DUNE", "FRANK HERBERT", "SCI-FI", 612, 5, 4),
("B007", "SAPIENS", "YUVAL NOAH HARARI", "HISTORY", 512, 4, 2),
("B008", "EDUCATED", "TARA WESTOVER", "BIOGRAPHY", 352, 3, 3),
("B009", "THE SILENT PATIENT", "ALEX MICHAELIDES", "THRILLER", 336, 6, 5),
("B010", "THINKING, FAST AND SLOW", "DANIEL KAHNEMAN", "PSYCHOLOGY", 499, 4, 4);

INSERT INTO MEMBER (MEMBER_ID, MEMBER_NAME, BOOK, BORROW_DATE, RETURN_DATE) VALUES
("M001", "ALICE SMITH", "B001", "2026-06-15", "2026-06-29"),
("M002", "BOB JONES", "B003", "2026-06-20", NULL),
("M003", "CHARLIE BROWN", "B003", "2026-06-22", "2026-07-02"),
("M004", "DIANA PRINCE", "B005", "2026-06-25", "2026-07-05"),
("M005", "ETHAN HUNT", "B006", "2026-06-28", NULL),
("M006", "FIONA GALLAGHER", "B007", "2026-07-01", NULL),
("M007", "GEORGE CLARK", "B007", "2026-06-10", "2026-06-24"),
("M008", "HANNAH ABBOTT", "B009", "2026-07-02", "2026-07-05"),
("M009", "IAN MALCOLM", "B001", "2026-06-05", "2026-06-19"),
("M010", "JULIA ROBERTS", "B003", "2026-07-04", NULL);

INSERT INTO BOOK_LOAN (LOAN_ID, MEMBER_ID, BOOK_ID, DAYS, TOTAL_FEE) VALUES
("L001", "M001", "B001", 14, 0.00),
("L002", "M002", "B003", 15, 5.50),
("L003", "M003", "B003", 10, 0.00),
("L004", "M004", "B005", 10, 0.00),
("L005", "M005", "B006", 7, 2.00),
("L006", "M006", "B007", 4, 0.00),
("L007", "M007", "B007", 14, 0.00),
("L008", "M008", "B009", 3, 0.00),
("L009", "M009", "B001", 14, 1.50),
("L010", "M010", "B003", 1, 0.00);""")

conn.commit()

tables = pd.read_sql("""SELECT * 
                        FROM sqlite_master 
                        WHERE type = "table";""", conn)
print("\n", tables)

books = pd.read_sql("""SELECT * 
                       FROM BOOKS;""", conn)
print("\n", books)

book_filtered = pd.read_sql("""SELECT BOOK_ID, BOOK_TITLE, AUTHOR
                               FROM BOOKS;""", conn)
print("\n", book_filtered)

science = pd.read_sql("""SELECT *
                         FROM BOOKS
                         WHERE GENRE = "SCIENCE";""", conn)
print("\n", science)

genre = pd.read_sql("""SELECT *
                       FROM BOOKS
                       WHERE (GENRE = "FICTION" OR GENRE = "HISTORY")
                             AND AVAILABLE > 0;""", conn)
print("\n", genre)

title = pd.read_sql("""SELECT * 
                       FROM BOOKS
                       WHERE BOOK_TITLE LIKE "THE%";""", conn)
print("\n", title)

page = pd.read_sql("""SELECT MAX(PAGES) AS "MOST PAGES",
                             MIN(PAGES) AS "LEAST PAGES"
                      FROM BOOKS;""", conn)
print("\n", page)

number = pd.read_sql("""SELECT MAX(COPIES) AS "MOST COPIES",
                             MIN(COPIES) AS "LEAST COPIES"
                      FROM BOOKS;""", conn)
print("\n", number)

conn.close()