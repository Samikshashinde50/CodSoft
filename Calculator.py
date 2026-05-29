# Advanced Simple Calculator

print("========== SIMPLE CALCULATOR ==========")

while True:

    # User input
    num1 = float(input("\nEnter First Number: "))
    num2 = float(input("Enter Second Number: "))

    # Operation menu
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")

    choice = input("Enter your choice (1-6): ")

    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print(f"\n✅ Result: {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"\n✅ Result: {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"\n✅ Result: {num1} × {num2} = {result}")

    elif choice == "4":

        if num2 == 0:
            print("\n❌ Cannot divide by zero!")

        else:
            result = num1 / num2
            print(f"\n✅ Result: {num1} ÷ {num2} = {result}")

    elif choice == "5":
        result = num1 ** num2
        print(f"\n✅ Result: {num1} ^ {num2} = {result}")

    elif choice == "6":
        result = num1 % num2
        print(f"\n✅ Result: {num1} % {num2} = {result}")

    else:
        print("\n❌ Invalid Choice!")

    # Continue option
    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
        print("\n🙏 Thank you for using the calculator!")
        break