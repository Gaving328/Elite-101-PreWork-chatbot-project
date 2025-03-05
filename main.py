print("Hello user!")
name = input("What is your name? ")
age = input("What is your age? ")
print("How may I help you, " + name + "?")

option = input("Would you like to see our settings, menu, exit, or if your food hasn't arrived, select 1: ").lower()

if option == "exit":
    print("Goodbye!")
    exit() 
elif option == "1":
    no_food = input("Would you want a refund or a re-delivery? ").lower()
    
    if no_food == "refund":
        print("Your order will be refunded. Thank you for your patience!")
    elif no_food == "re-delivery":
        print("Thank you for your patience! Your food will be delivered soon!")
    else:
        print("Invalid option. Please select either 'refund' or 're-delivery'.")

