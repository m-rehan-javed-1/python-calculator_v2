print("\n=== Python Calculator (2nd Edition) ===\n")
def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error. Division by zero is not possible."
    else:
        return a/b

def input_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Please enter a number.")


def calculator():

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    print("\nChoose operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")

    choice = input("\nEnter your choice (+,-,*,/): ")
    if choice == "+":
        result = add(num1, num2)
    elif choice == "-":
        result = subtract(num1, num2)
    elif choice == "*":
        result = multiply(num1, num2)
    elif choice == "/":
        result = divide(num1, num2)
    else:
        print("\nInvalid operation selected.")
        return
    print("\nResult: ",result)

while True:
    calculator()
    repeat = input("\nDo you want to continue? (y/n): ").lower()
    if repeat != "y":
        print("\nThank you for using this calculator!.")
        break