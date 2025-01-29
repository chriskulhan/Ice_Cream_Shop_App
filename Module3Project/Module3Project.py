#Ice Cream Shop Application
#Author: Chris Kulhanek (following instructions from Dr. Mary Lebens ITEC capstone class) 
#Date: 1/29/2025

#Store our ice cream shop's menu items
flavors = ["mint-chocolate chip", "coconut", "vanilla"]
toppings = ["chocolate syrup", "walnuts", "cherries"]
prices = {"scoop": 2.50, "topping": 0.50}

#define/declare a new function (modularized code, does a single task)
def display_menu(): 
    #shows available flavors and toppings to the customer
    print("\n===Welcome to the Ice Cream Shop! ===")
    print("\nAvailable flowers:")

    #Loop through the flavor list and show each flavor,
    #then do the same for toppings
    #use a for loop because you know the number of flavors
    for flavor in flavors: 
        print(f" - {flavor}")
        #TODO add the concatenation way to do this

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    #display prices to user 
    print("\nPrices")        
    print(f"Scoops: ${prices['scoop']:.2f} each")
    #TODO see if you can use just the place of the , not the name in the {prices['0']}
    print(f"toppings: ${prices['topping']:.2f)} each")


def get_flavors():
    #Get ice cream flavor from the customer
    chosen_flavors = []

    #use a while loop to keep taking orders until the customer is done ordering    
    #include a break to prevent an infinite loop
    while True:
        try:
            #code to execute:Prompt use to choose their scoops
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            #validate teh input

            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops. ")
        except ValueError:
            print("Please enter a number.")    
    
    #Prompt the user to enter the ice cream flavor
    print("\n For each scoop, enter the flavor you'd like:")
    
    #prompts for each scoop of ice cream
    for i in range(num_scoops):
        #handles the users input and validation
        while True:
            #.lower() makes input lowercase: 
            flavor = input(f"Scoop {i+1}: ").lower()
            #Check to see if the flavor is one that's in the shop's list
            if flavor in flavors: 
                #add the user selected flavor to the new list 
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")

    #Return the calling function, the number of scoops the user wants
    #and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings(): 
    #gets toppings from the customer
    #start with an empty list
    chosen_toppings = []

    #use a while loop to prompt the user for the toppings, until they are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        #test if the user is done ordering toppings
        #== is boolean True/false
        if topping == 'done': 
            break

        #test if the topping is in the list of toppings for the shop
        if topping in toppings: 
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")    
    
    #Return the list of user chosen toppings
    return chosen_toppings         

#Main function (this is called and run first, director of the show)
def main():
    display_menu()

#automatically executes the main function when the application runs
if __name__ == "__main__":
    main()    

    #terminal type: 