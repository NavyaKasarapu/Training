correct_pin = "1234"
attempts = 0

while attempts < 3:
    user_pin = input("Enter PIN: ")
    attempts += 1
    
    if user_pin == correct_pin:
        print("PIN accepted! Welcome.")
        break
    else:
        print(f"Wrong PIN. {3-attempts} attempts left.")
        
else:
    print("Card blocked. Contact support.")
