print("Hello user!")
name = input("What is your name? ")
age = input("What is your age? ")
print("How may I help you, " + name)

option = input("Would you like to see our settings, menu, or exit? ").lower()
if option == "exit":
    print("Goodbye!")
    exit() 
else:
    print("You selected:", option)