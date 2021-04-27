import calculator_module

print(" Select any one Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")


while True:
    choice = int(input("Enter choice (1/2/3)"))
    if choice in (1,2,3):
        num1 = float(input("Enter First Number"))
        num2 = float(input("Enter second number"))

        if choice == 1:
            print(num1, "+", num2, "=", calculator_module.add(num1,num2))
        elif choice == 2:
            print(num1, "-", num2, "=", calculator_module.sub(num1,num2))
        elif choice == 3:
            print(num1, "*", num2, "=", calculator_module.mul(num1,num2))
        else:
            print("Wrong Choice")

    else:
        print("Invalid input")
