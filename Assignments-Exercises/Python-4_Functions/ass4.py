def create_greeting(name):

    print(f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!")


try:
     name = input("Enter your name: ")
     create_greeting(name)
    
except ValueError:
    print("Invalid input. Please enter a string.")

