#Тестовий файл просто щоб заповнить БД книгами

from connect_db import connectdb
import random

random_title = ["The Harry Potter Series", "1984", "Pride and Prejudice", "The Great Gatsby", "War and Peace", "Murder on the Orient Express", "The Adventures of Tom Sawyer", "To Kill a Mockingbird", "One Hundred Years of Solitude", "The Old Man and the Sea"]
random_author = ["J.K. Rowling", "George Orwell", "Jane Austen", "F. Scott Fitzgerald", "Leo Tolstoy", "Agatha Christie", "Mark Twain", "Harper Lee", "Gabriel Garcia Marquez", "Ernest Hemingway"]
random_categore = ["Mathematics", "English Language", "History", "Physics", "Chemistry", "Biology", "Geography", "Art", "Physical Education", "Computer Science"]

def new_count(count):
    new_c = random.randint(1,10)
    if count > new_c:
        return new_c
    else:
        new_count(count)

books_dict = {}
for i in range(10):
    books_dict["isbn"] = random.randint(0,99999)
    books_dict["bookstitle"] = random.choice(random_title) + random.choice(random_title)
    books_dict["booksauthor"] = random.choice(random_author)
    count = random.randint(5,30)
    books_dict["count"] = count
    books_dict["count_now"] = new_count(count)
    books_dict["grade"] = random.randint(1,10)
    books_dict["category"] = random.choice(random_categore)
    connectdb.cursor.execute('INSERT INTO books (isbn,bookstitle,booksauthor,count,count_now,grade,category) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (books_dict["isbn"],
                            books_dict["bookstitle"],
                            books_dict["booksauthor"],
                            books_dict["count"],
                            books_dict["count_now"],
                            books_dict["grade"],
                            books_dict["category"])
                            )
    connectdb.conn.commit()
