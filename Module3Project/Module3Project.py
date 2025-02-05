#Ice Cream Shop Application
#Author: Chris Kulhanek (following instructions from Dr. Mary Lebens ITEC capstone class) 
#Date: 1/29/2025

#Store our ice cream shop's menu items
cone_types = ["cake", "sugar", "waffle"]
flavors = ["mint-chocolate chip", "coconut", "vanilla", "caramel swirl", "praline pecan", "chocolate chunk"]
toppings = ["chocolate syrup", "walnuts", "cherries"]
prices = {
    "scoop": 2.50, 
    "topping": 0.50
    }

#define/declare a new function (modularized code, does a single task)
def display_menu(): 
    #shows available flavors and toppings to the customer
    print("\n=== Welcome to the Ice Cream Shop! ===")

    #add cone types to the display menu:
    print("\nAvailable types of cone:")

    #Loop through the types of cones:
    for cone in cone_types:
        print(f" - {cone}")
        
    print("\nAvailable flavors:")

    #Loop through the flavor list and show each flavor,
    #then do the same for toppings
    #use a for loop because you know the number of flavors
    for flavor in flavors: 
        print(f" - {flavor}")
        #TODO add the concatenation way to do this (extra, not required)

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    #display prices to user 
    print("\nPrices")        
    print(f"Scoops: ${prices['scoop']:.2f} each")
    #TODO see if you can use just the place of the , not the name in the {prices['0']} (extra)
    print(f"toppings: ${prices['topping']:.2f} each")

def get_cone():
    #get cone type from the customer
    chosen_cone = []

    #ask the user what type of cone they would like:
    cone = input("Which type of cone would you like: cake, sugar, or waffle?").lower()
   
    while True:
        try:
            #make sure they choose a cone type you have:
            if cone in cone_types:   
                chosen_cone.append(cone)
                print(f"You chose {cone}!")
                break
        except ValueError:
            print("Please choose cake, sugar, or waffle.") 
    
    #return the cone type to the calling function
    return chosen_cone        

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

def calculate_total (num_scoops, num_toppings):
    #Calculates the total cost of the order
    scoop_cost = num_scoops * prices["scoop"]
    #prices is a dictionary, look up price
    topping_cost = num_toppings * prices["topping"]
    #total cost of the order: 
    return scoop_cost + topping_cost

def print_receipt(chosen_cone, num_scoops, chosen_flavors, chosen_toppings):
    #prints a nice receipt for the customer
    print("\n=== Your Ice Cream Order ===")
    print(f"\n{chosen_cone.title()} + Cone")
    for i in range(num_scoops):
        #i is the variable that will hold the number for the current scoop
        #.title will give this title case:
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")
    if chosen_toppings:
        print("\nToppings: ")
        #loop through the list of toppings, use for because # in list is known
        for topping in chosen_toppings:
            print(f" - {topping.title()}")

    #Print the total outside of the if loop
    #new variable called total:
    #use len to find how many toppings (length of the )
    total = calculate_total(num_scoops, len(chosen_toppings))      
    print(f"\nTotal: ${total:.2f}")

    #save the order to a file 
    #created new file object and allow it to append using 'a'
    with open("daily_orders.txt", "a" ) as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")


#Main function (this is called and run first, director of the show)
def main():
    display_menu()

    #call get_cone function, returns type of cone
    chosen_cone = get_cone()

    #call get_flavors function, returns number of scoops and list of flavors
    num_scoops, chosen_flavors = get_flavors()

    #Call the get_toppings functions, returns the list of toppings
    chosen_toppings = get_toppings()

    #Display and order summary
    #print("\nOrder Summary:")
    #print(f"Scoops: {chosen_flavors}")
    #print(f"Toppings: {chosen_toppings}")

    #Display receipt:
    print_receipt(num_scoops, chosen_flavors, chosen_toppings)

#automatically executes the main function when the application runs
if __name__ == "__main__":
    main()    

    #terminal type: 