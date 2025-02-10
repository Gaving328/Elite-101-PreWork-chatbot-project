print("Hello user!")
name = input("What is your name? ")
age = input("What is your age? ")
print("How may I help you, " + name)

option = input("Would you like to see our settings, menu, exit, and has your food arived if not select 1 ").lower()
if option == "exit":
    print("Goodbye!")
    exit() 
elif option == "1":
    no_food = input("Would you want a refund or a re-delivery? ")
    no_food == "refund":
        print("You're order will be refunded thank you for your patience!")
    no_food == "re-delivery"
        print("Thank you for you patience you're food will be delivered soon!"
