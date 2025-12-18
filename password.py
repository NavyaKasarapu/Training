a = input("Enter password: ")
chars = list(a)
length = len(chars)

if length == 6:
    print("Too short")
elif length > 6:
    has_letter = False
    has_digit = False
    
    for char in chars:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
    
    if has_letter and has_digit:
        print("Strong")
    elif has_letter:
        print("Too weak")
    else:
        print("Invalid")
