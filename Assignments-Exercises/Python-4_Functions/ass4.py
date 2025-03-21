def create_greeting(name: str):
    #returns template 
    return f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

 
try:
    user_name = input("Enter your name: ") #user inputs name 
    print(create_greeting(user_name))
    
except ValueError:
    print("Invalid input. Please enter a valid name.")

