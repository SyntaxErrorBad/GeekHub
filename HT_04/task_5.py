while True:
    try:
        user_input = input("Enter a valid integer: ")
        number = int(user_input)
        break  # Exit the loop if the input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"You entered a valid integer: {number}")
