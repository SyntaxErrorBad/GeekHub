class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

try:
    num = int(input("Enter an integer: "))
    
    if num < 0:
        raise NegativeValueError(num) 
    
    print(f"The entered integer is: {num}")
except NegativeValueError as e:
    print(f"Error: Negative value ({e.value}) is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
