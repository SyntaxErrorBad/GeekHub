class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

try:
    age = int(input("Enter your age: "))
    
    if age < 18 or age > 120:
        raise InvalidAgeError(age)
    
    print(f"Your age is: {age}")
except InvalidAgeError as e:
    print(f"Error: Invalid age ({e.age}). Age must be between 18 and 120.")
except ValueError:
    print("Error: Invalid input. Please enter a valid age as an integer.")
