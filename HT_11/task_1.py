class Calc:
    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        result = a + b
        self.last_result = result
        return result

    def subtract(self, a, b):
        result = a - b
        self.last_result = result
        return result

    def multiply(self, a, b):
        result = a * b
        self.last_result = result
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.last_result = result
            return result
        else:
            print("Error: Division by zero.")
            return None

calculator = Calc()

print("last_result -->", calculator.last_result)

result_add = calculator.add(1, 1)
print("1 + 1 =", result_add)
print("last_result -->", calculator.last_result)

result_multiply = calculator.multiply(2, 3)
print("2 * 3 =", result_multiply)
print("last_result -->", calculator.last_result)

result_multiply_again = calculator.multiply(3, 4)
print("3 * 4 =", result_multiply_again)
print("last_result -->", calculator.last_result)


