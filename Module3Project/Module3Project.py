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

#Main function (this is called and run first, director of the show)
def main():
    display_menu()

#automatically executes the main function when the application runs
if __name__ == "__main__":
    main()    

    #terminal type: 