

try: 
    # Get user age
    user_input = int(input("Please enter your age: "))


    if user_input < 0:
        raise ValueError("Age cannot be negative.")
    if user_input < 13:
        print("You are categorized as: Child")
    elif user_input < 20:
        print("You are categorized as: Teenager")
    elif user_input < 60:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")

except ValueError:
    print("Invalid input: Age should be a number.")



