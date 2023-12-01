import sqlite3
import os
import random


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

class WorkWithDBBooks:

    def take_count(self):
        self.cursor.execute("SELECT count FROM books")
        return self.cursor.fetchall()

    def take_count_one(self,title):
        self.cursor.execute("SELECT count FROM books WHERE bookstitle = ?",(title,))
        return self.cursor.fetchone()
    
    def take_count_one_now(self,title):
        self.cursor.execute("SELECT count_now FROM books WHERE bookstitle = ?",(title,))
        return self.cursor.fetchone()

    def find_book_by_title(self,title):
        self.cursor.execute("SELECT * FROM books WHERE bookstitle = ?",(title,))
        return self.cursor.fetchall()

    def find_books_by_author(self,author):
        self.cursor.execute("SELECT bookstitle FROM books WHERE booksauthor = ?",(author,))
        return self.cursor.fetchall()
    
    def find_books_by_isbn(self,isbn):
        self.cursor.execute("SELECT bookstitle FROM books WHERE isbn = ?",(isbn,))
        return self.cursor.fetchall()
    
    def find_books_by_grade(self,grade):
        self.cursor.execute("SELECT bookstitle FROM books WHERE grade = ?",(grade,))
        return self.cursor.fetchall()

    def add_book_in_db_by_title(self,title,count):
        new_count = self.take_count_one_now(title)[0] + count
        self.cursor.execute('UPDATE books SET count_now = ? WHERE bookstitle = ?', (new_count, title))
        self.conn.commit()

    def remove_book_in_db_by_title(self,title,count):
        new_count = self.take_count_one_now(title)[0] - count
        self.cursor.execute('UPDATE books SET count_now = ? WHERE bookstitle = ?', (new_count, title))
        self.conn.commit()

class WorkWithDBUsers:
    def register_user(self,role,name,age,gender,arg):
        if role == "teacher":
            try:
                self.cursor.execute('INSERT INTO users_teacher (name,role,age,subject,gender) VALUES (?, ?, ?, ?, ?)', (name,role,age,arg,gender))
                self.conn.commit()
                return True
            except:
                return False
        else:
            try:
                self.cursor.execute('INSERT INTO users_student (name,role,age,grade,gender) VALUES (?, ?, ?, ?, ?)', (name,role,age,arg,gender))
                self.conn.commit()
                return True
            except:
                return False

    def login_user(self,role,name,age,gender,arg):
        if role == "teacher":
            try:
                self.cursor.execute('SELECT role FROM users_teacher WHERE name = ? AND age = ? AND subject = ? AND gender = ?', 
                                    (name,age,arg,gender))
                if self.cursor.fetchall() is not None:
                    return True
                return False
            except:
                return False
        else:
            try:
                self.cursor.execute('SELECT * FROM users_student WHERE name = ? AND role = ? AND age = ? AND grade = ? AND gender = ?', 
                                    (name,role,age,arg,gender))
                if self.cursor.fetchall() is not None:
                    return True
                return False
            except:
                return False

class ConnectDB(WorkWithDBBooks,WorkWithDBUsers):
    def __init__(self) -> None:
        self.conn = sqlite3.connect(os.path.join(parent_directory, 'library.db'))
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                isbn INTEGER PRIMARY KEY AUTOINCREMENT,
                bookstitle TEXT UNIQUE,
                booksauthor TEXT,
                count INTEGER,
                count_now INTEGER,
                grade INTEGER DEFAULT 1,
                category TEXT
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users_teacher (
                name TEXT UNIQUE,
                role TEXT,
                age INTEGER,
                subject TEXT,
                gender TEXT
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users_student (
                name TEXT UNIQUE,
                role TEXT,
                age INTEGER,
                grade TEXT,
                gender TEXT
            )
        ''')
        self.conn.commit()




connectdb = ConnectDB()