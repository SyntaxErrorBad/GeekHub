# 2. Створіть за допомогою класів та продемонструйте свою реалізацію
# шкільної бібліотеки (включіть фантазію). Наприклад вона може містити класи Person,
# Teacher, Student, Book, Shelf, Author, Category і.т.д.
from connect_db import connectdb

class Person:
    def __init__(self, name, age, role,gender):
        self.name = name
        self.age = age
        self.role = role
        self.gender = gender

    
class Teacher(Person):
    def __init__(self, name, age, role, gender, subject):
        super().__init__(name, age, role, gender)
        self.subject = subject
        self.subject_school = ["Mathematics", "English Language", "History", "Physics", "Chemistry", "Biology", "Geography", "Art", "Physical Education", "Computer Science"]
    
    def register_teacher(self):
        if self.subject in self.subject_school:
            if self.gender in ("1", "2"):
                return connectdb.register_user(self.role,self.name,self.age,self.gender,self.subject)
        return False

    def login_teacher(self):
        if self.subject in self.subject_school:
            if self.gender in ("1", "2"):
                return connectdb.login_user(self.role,self.name,self.age,self.gender,self.subject)

        return False


class Student(Person):
    def __init__(self, name, age, role, gender, grade):
        super().__init__(name, age, role, gender)
        self.grade = grade
        self.grade_school = [i for i in range(1,12)]

    def register_student(self):
        if int(self.grade) in self.grade_school:
            if self.gender in ("1", "2"):
                if connectdb.register_user(self.role,self.name,self.age,self.gender,self.grade):
                    return True
        return False

    def login_student(self):
        if int(self.grade) in self.grade_school:
            if self.gender in ("1", "2"):
                return connectdb.login_user(self.role,self.name,self.age,self.gender,self.grade)

        return False


class Book:
    def __init__(self, title, author=None, category=None, isbn=None,grade=None):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn
        self.grade = grade
    
    def get_count_all_books(self):
        return sum([int(_[0]) for _ in connectdb.take_count()])

    def get_count_book(self):
        if self.check_book_in_shelf():
            return connectdb.take_count_one_now(self.title)[0]
        return "The book does not exist in Shelf"

    def check_book_in_shelf(self):
        if connectdb.find_book_by_title(self.title) is None:
            return False
        return True


        


class Shelf(Book):
    def __init__(self,title=None,author=None, category=None, isbn=None, grade=None):
        super().__init__(title, author, category, isbn, grade)

    def add_book_in_shelf_count(self, count=1):
        if self.check_is_full_book(count):
            connectdb.add_book_in_db_by_title(self.title,count)
            return "All good, U add book"
        return "Something Wrong Try again"
    
    def remove_book_in_shelf_count(self, count=1):
        if self.check_is_zero_book(count):
            connectdb.remove_book_in_db_by_title(self.title,count)
            return "Take u book!"
        return "Something Wrong Try again"

    def find_book_in_shelf_by_author(self):
        books = connectdb.find_books_by_author(self.author)
        print(books)
        return '\n'.join([book[0] for book in books])
    
    def find_book_in_shelf_by_isbn(self):
        books = connectdb.find_books_by_isbn(self.isbn)
        print(books)
        return '\n'.join([book[0] for book in books])
    
    def find_book_in_shelf_by_grade(self):
        books = connectdb.find_books_by_grade(self.grade)
        print(books)
        return '\n'.join([book[0] for book in books])
    
    def check_is_full_book(self,count):
        if connectdb.take_count_one_now(self.title)[0] == connectdb.take_count_one(self.title)[0]:
            return False
        else:
            free_books = connectdb.take_count_one(self.title)[0] - connectdb.take_count_one_now(self.title)[0]
            if free_books >= count:
                return True
            else:
                return False
    
    def check_is_zero_book(self,count):
        if connectdb.take_count_one_now(self.title)[0] == 0:
            return False
        else:
            if connectdb.take_count_one_now(self.title)[0] >= count:
                return True
            else:
                return False


def take_books_info():
    title = input("Books title: ")
    author = input("Books author(write 'No' if forget)")
    category = input("Books category(write 'No' if forget)")
    isbn = input("Books isbn(write 'No' if forget)")
    grade = input("Books grade(write 'No' if forget)")
    shelf = Shelf(title,
                  None if author == "No" else author,
                  None if category == "No" else category,
                  None if isbn == "No" else isbn,
                  None if grade == "No" else grade
                  )
    return shelf


def work_with_books(action):
    shelf = take_books_info()
    if action == "1":
        print(shelf.remove_book_in_shelf_count(int(input("Pls enter Books count: "))))
    elif action == "2":
        print(shelf.add_book_in_shelf_count(int(input("Pls enter Books count: "))))
    elif action == "3":
        print(f"Books in db: {shelf.get_count_book()}")


def use_bookshelf():
    quest_book = input("What u want?\nTake book(1)\nPut book(2)\nFind number books(3)\nExit(4)\nAnswer: ")
    if quest_book in ("1","2","3"):
        work_with_books(quest_book)
    elif quest_book == "4":
        exit()
    else:
        print("Wrong Answer")
    use_bookshelf()

def check_users(login):
    role = input("Who you are?\nTeacher(1)\nStudent(2)\n Answer: ")
    if role == "1":
        subjects = ["Mathematics", "English Language", "History", "Physics", "Chemistry", "Biology", "Geography", "Art", "Physical Education", "Computer Science"]
        teacher = Teacher(input("Name: "),int(input("Age: ")),"teacher",input("Gender\nmale(1)\nfemale(2): "),input(f"subjects: {subjects} choose only one: "))
        if login == "1":
            check = teacher.register_teacher()
            if not check:
                print("Wrong answer!")
                start()
        else:
            check = teacher.login_teacher()
            print(check)
            if not check:
                print("Wrong answer!")
                start()


    elif role == "2":
        grades = [i for i in range(1,12)]
        student = Student(input("Name: "),int(input("Age: ")),"student",input("Gender\n male(1)\n female(2): "),input(f"grade: {grades} choose only one: "))
        if login == "1":
            check = student.register_student()
            if not check:
                print("Wrong answer!")
                start()
        else:
            check = student.login_student()
            if not check:
                print("Wrong answer!")
                start()
    else:
        print("Wrong answer!")
        start()
    
    use_bookshelf()


def start():
    question = input("Want Register?:\nYes(1)\nNo(2)\nExit(3)\nAnswer: ")
    if question == "1" or question == "2":
        check_users(question)
    elif question == "3":
        exit()
    else:
        print("Wrong answer!")
        start()



def main():
    start()


if __name__ == "__main__":
    main()
