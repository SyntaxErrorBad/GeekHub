# 2. Створіть за допомогою класів та продемонструйте свою реалізацію
# шкільної бібліотеки (включіть фантазію). Наприклад вона може містити класи Person,
# Teacher, Student, Book, Shelf, Author, Category і.т.д.
class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_role(self):
        return self.role


class Teacher(Person):
    def __init__(self, name, age, role, subject):
        super().__init__(name, age, role)
        self.subject = subject

    def get_subject(self):
        return self.subject


class Student(Person):
    def __init__(self, name, age, role, grade):
        super().__init__(name, age, role)
        self.grade = grade

    def get_grade(self):
        return self.grade


class Book:
    def __init__(self, title, author, category, isbn):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_category(self):
        return self.category

    def get_isbn(self):
        return self.isbn


class Shelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = []

    def get_capacity(self):
        return self.capacity

    def add_book(self, book):
        if self.is_full():
            raise Exception("Стеллаж переповнений")
        else:
            self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def is_full(self):
        return len(self.books) == self.capacity


class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Category:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    

class Grade:
    def __init__(self, student_grade, grade):
        self.grade = grade
        self.student_grade = student_grade

    def get_grade(self):
        return self.grade
    
    def get_student_grade(self):
        return self.student_grade
    
    def check_grade(self):
        return self.student_grade == self.grade
    

teacher = Teacher("John Doe", 45, "Teacher", "Math")
print(teacher.get_name())  
print(teacher.get_age())  
print(teacher.get_role())  
print(teacher.get_subject())  


student = Student("Jane Smith", 16, "Student", 10)
print(student.get_name())
print(student.get_age())  
print(student.get_role())  
print(student.get_grade())  


book = Book("The Adventures of Tom Sawyer", "Mark Twain", "Adventure", "90730378383")
print(book.get_title())
print(book.get_author())  
print(book.get_category())  
print(book.get_isbn())  

shelf = Shelf(10)
shelf.add_book(book)
print(shelf.get_capacity())

author = Author("Mark", "Twain")
print(author.get_name())
print(author.get_surname())

category = Category("Ukr History")
print(category.get_name())

grade = Grade(8, 8)
print(grade.get_grade())
print(grade.get_student_grade())
print(grade.check_grade())
