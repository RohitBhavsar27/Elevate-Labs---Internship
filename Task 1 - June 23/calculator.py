# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def main():
    print("\nSimple CLI Calculator")
    print("----------------------")
    
    while True:
        print("\nSelect operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("----------------------")

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input, try again!")


if __name__ == "__main__":
    main()
