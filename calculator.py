while True:
    print("Menu")
    print("1. Add")
    print("2. Sub")
    print("3. Mult")
    print("4. Div")
    print("5. Exit")

    c = int(input("Enter your choice: "))

    if c == 5:
        print("Exit")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if c == 1:
        print("Sum:", a + b)
    elif c == 2:
        print("Subtract:", a - b)
    elif c == 3:
        print("Multiplication:", a * b)
    elif c == 4:
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Division:", a / b)
    else:
        print("Invalid choice")
