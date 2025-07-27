'''
Project:Calculator

Description:
This is a command-line calculator that performs basic arithmetic operations — addition, subtraction, multiplication, and division. It demonstrates user input handling, conditional logic, and formatted output in Python.
'''
# code:

def calculator():
    print("----- Simple Calculator -----")
    
    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Display operation menu
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform operation
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero.")
        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers.")

# Run the calculator
calculator()
