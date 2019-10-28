class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        raise ValueError("Cannot divide by 0")

if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(12, 10))
    print(calculator.subtract(100, 30))
    print(calculator.multiply(1000, 48))
    print(calculator.divide(50, 10))
    print(calculator.divide(334, 0))