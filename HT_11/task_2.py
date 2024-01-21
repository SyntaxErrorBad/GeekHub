# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати
# якісь аргументи, які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession
# (його не має інсувати під час ініціалізації).
# 1 спосіб
class Person:
    profession = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"{self.name}'s age is {self.age} years.")

    def print_name(self):
        print(f"Name: {self.name}")

    def show_all_information(self):
        print(f"Name: {self.name}, Age: {self.age},{self.profession}")


person1 = Person(name="John", age=25)
person2 = Person(name="Jane", age=30)


person1.profession = "Engineer"
person2.profession = "Teacher"


person1.show_all_information()
person2.show_all_information()


# 2 спосіб
class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"{self.name}'s age is {self.age} years.")

    def print_name(self):
        print(f"Name: {self.name}")

    def show_all_information(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person1(name="John", age=25)
person2 = Person1(name="Jane", age=30)
setattr(person1, "profession", "Engineer")
setattr(person2, "profession", "Teacher")
print(person1.__dict__)
print(person2.__dict__)
print(person1.profession)
print(person2.profession)
person1.show_all_information()
person2.show_all_information()
