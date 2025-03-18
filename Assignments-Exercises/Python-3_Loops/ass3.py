def for_funct():
    list = ["Ice cream", "Chocolate", "Candy", "Cake", "Cookie"]
    for food in list:
        print(f"- {food}")

def while_funct():
    while True:
        try:
            cd_start = int(input("Please enter a starting number: "))

            if cd_start <= 0:
                print("Invalid input. Please try again.")
                
            else:
                print("countdown start.")
                while cd_start > 0:
                    print(cd_start)
                    cd_start -= 1
                print("countdown complete!")        
    #break
        except ValueError: 
            print("Invalid input. Please enter an integer.")



#for_funct()
while_funct()