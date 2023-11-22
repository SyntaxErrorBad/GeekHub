class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profession = None

    def show_age(self):
        print(f"{self.name}'s age is {self.age} years.")

    def print_name(self):
        print(f"Name: {self.name}")

    def show_all_information(self):
        print(f"Name: {self.name}, Age: {self.age}, Profession: {self.profession}")


person1 = Person(name="John", age=25)
person2 = Person(name="Jane", age=30)


person1.profession = "Engineer"
person2.profession = "Teacher"


person1.show_all_information()
person2.show_all_information()