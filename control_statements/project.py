num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter your choice (+ - * =): ")

if choice == "+":
    print(f'Addition: {num1+num2}')
elif choice == "-":
    print(f'Subtraction: {num1-num2}')
elif choice == "*":
    print(f'Multiplication : {num1*num2}')
else:
    print("Invalid choice")

