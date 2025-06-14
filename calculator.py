
# student directory
class Calculator:
    def __init__(self, num1=0, num2=0, operation=''):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
    
    def inputs(self):
        self.num1 = int(input("\nEnter the number 1:\n"))
        self.num2 = int(input("\nEnter the second number:\n"))
        self.operation = input("\nEnter the operation (+, -, *, /):\n")
        if self.operation == '/' and self.num2 == 0:
            print("\nDivision by 0 is not possible.")
            self.num2 = int(input("Enter another second number:\n"))

    def calc(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '*':
            return self.num1 * self.num2
        elif self.operation == '/':
            return self.num1 / self.num2
        elif self.operation == '-':
            return abs(self.num1 - self.num2)
        else:
            return "Invalid operation"

# Main program
print("Welcome to calculator")
print("\n-------------------------------------")
calc_obj = Calculator()
calc_obj.inputs()
result = calc_obj.calc()
print("Result:", result)
