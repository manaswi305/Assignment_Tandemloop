class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation"

a = input("Enter the first number: ")
b = input("Enter the second number: ")
operation = input("Enter the type of operation (Addition, Subtraction, Multiplication, Division): ")
calc = Calculator(a, b, operation)
print("Result:", calc.calculate())
