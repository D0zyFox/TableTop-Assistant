import random

#gold value and bag list for global usage
player_bag = []
player_gold = int(0)

shopInventory = {
        "Rations": 3,        
        "Rope": 5,    
        "Torch": 1,      
        "Bedroll": 5,        
        "Waterskin": 2,        
        "Crowbar": 7,          
        "Grappling Hook": 10,     
        "Lantern": 5, 
        "Oil flask": 1,
        "Short Sword": 10,
        "Longbow": 25,
        "Arrows": 10,
        "Chain Mail": 50,
        "Shield": 15,
        "Daggers": 2,
    }

#Items Dictionaries with gold values $
common_items = {
        "Potion of Healing": 10,
        "Rusty Sword": 4,
        "Old Boots": 3,
        "Simple Bow": 5,
        "Torch": 1,
        "Ripped Shirt": 2,
        "Bread": 1,
    }
uncommon_items = {
        "Spyglass": 20,
        "Bottle of Poison": 15,
        "Fancy Shirt": 11,
        "Treasure Map": 17,
        "Gemstone": 25,
    }
rare_items = {
        "Staff of Netherwind": 35,
        "Amulet of Healing": 30,
        "Spear of Suffering": 50,
    }

def login(): 
    global user_input
    user_input = input("Enter your username:")
    user_name = "Hamish"
 # The user imput inputs their login infomation if its incorrct it will ask again   
    while user_input != user_name:
        print("username incorrect try again")
        user_input = input("Enter your username:")
    
    print() 
    password_input = input("Hello " +  user_input  + ", please enter your password:")
    password_name = "ILoveDnd"
 # Same for the password   
    while password_input != password_name:
        print("password incorrect try again")
        password_input = input("Hello " +  user_input  + ", please enter your password:")
    print("Welcome " + user_input)

def mainmenu(): 
    
    while True:
        print("Please choose from the following options:")
        print()
        mainmenu_items = ["1:Loot Generator", "2:Potion Maker", "3:Shop", "4:Bag", "5:Quit"]
        
        for mainselection in mainmenu_items:
            print(mainselection)
        
        mainmenu_selection = input() #The user makes a selection it will the call upon the selected function, or quit the program
        if mainmenu_selection == "1":
            lootgenerator()
        elif mainmenu_selection == "2":
            potionmaker()
        elif mainmenu_selection == "3":
            shop()
        elif mainmenu_selection == "4":
            bag()
        elif mainmenu_selection == "5":
             print()
             print("See you next time " + str(user_input))
             print("---------------------")
             break #program will end if 5 is selected
        else: 
            print("Please choose from the following options:") #If the user doesn't a correct value it will continue asking
        
def bag():
    
    if len(player_bag) == 0:   # two options if bag has options or not
        print("Your bag is empty")
        print("you have " + str(player_gold) + " gold in your bag")
        print()
        return
    else:
        print("Current bag inventory:")
        print("----------------------")
        for bag_content in player_bag: # neatly display bag content and gold plater bag and gold found at beginning of the program
            print(bag_content)
        print("you have " + str(player_gold) + " gold in your bag")
        print("----------------------")
        print()

    
def lootgenerator():
    print()
    print("Choose encounter difficulty:")
    lootmenu_selection_list = ["1:Easy", "2:Medium", "3:Hard", "4:Menu"]
    
    for loot_select in lootmenu_selection_list: # selection for which generator to activte
        print(loot_select)
    lootmenu_user_selection = input()
    
    #refer to generateloot function
    if lootmenu_user_selection == "1": 
        generateloot(3, "commonitems")

    elif lootmenu_user_selection == "2":
        generateloot(2, "uncommonitems")
    
    elif lootmenu_user_selection == "3":
        generateloot(1, "rareitems")
    
    else:
        return
    
def potionmaker():
    
    #Lists for ingredients and selections
    ingredient_list_herb = ("Moonflower", "Nightshade Berries", "Lavender Sprig", "Wolfsbane", "Ginseng Root", "Sage Leaves", "Dandelion Root", "Belladonna", "Thyme", "Rosemary", "Mandrake Root", "Basilisk Vine", "Marigold Petals", "Aloe Vera Gel", "Yarrow")
    ingredient_list_element = ("Fairy Dust", "Mermaid Tears", "Essence of Night", "Essence of Fire", "Shadow Moss", "Elven Wine", "Phoenix Feather", "Cloud Essence", "Pixie Wings", "Thunderstorm Water", "Eternal Flame Ember", "Rainbow Droplet")
    potionmenu_selection_list1 = []
    potionmenu_selection_list2 = []

    print()
    print("The cauldron bubbles with anticipation")
    print("Choose a herb to throw in 1-3")
    print()
    potionmenu_selection_list1 = random.sample(ingredient_list_herb, 3) #random ingredient selection

    for ingredient_select1 in potionmenu_selection_list1:
        print(ingredient_select1)
    
    lootmenu_user_selection = input()
    
    #ingredient selection
    if lootmenu_user_selection <= "3":
        print("'Bubble Bubble', throw in your next ingredient:")
        print()
        
        potionmenu_selection_list2 = random.sample(ingredient_list_element, 3)
        for ingredient_select2 in potionmenu_selection_list2:
            print(ingredient_select2)       #Random ingredient Selection
        print("--------------------------------")
        print("Place in the next ingredient 1-3")

        failure_factor = random.randint(1, 10)
        lootmenu_user_selection = input()
        
        #Number generation if the potion will fail
        if failure_factor <= int("3"):
            print("The potion exploded")
            print()
            return
        elif failure_factor >= int("4"):
            print("Brew successful, fancy potion added to bag")
            print()
            player_bag.append("Brewed Potion")
    else:  
        return

def shop(): # View shop inventory
    print()
    print("Shop Inventory:")
    print("-------------------")
    
    for item, price in shopInventory.items():
        print(f"{item}: {price} gold")  # Display shop items and prices
    
    print("What would you like to buy, type item name")
    print("-------------------")
    print("type 0 to return to main menu")
    
    shopAnswer = input()
    if shopAnswer == str("0"):
            return
    elif shopAnswer in shopInventory: 
        shopPurchase(shopAnswer)  # Takes shop answer into ShopPurchase function
    else:
        print("Invalid item selection. Please try again.")
        shop()  # Loop back if the input is invalid

def shopPurchase(shopAnswer): # Purchasing Items
    global player_gold 
    item_price = shopInventory[shopAnswer]
    print()
    
    if player_gold >= item_price:
        player_gold -= item_price  # Deduct the item's price from the player's gold
        print(f"You successfully bought {shopAnswer} for {item_price} gold.")
        print(f"Remaining gold: {player_gold} gold.")
        player_bag.append(shopAnswer)   # Add purchased item to global bag
    else:
        print(f"Not enough gold to buy {shopAnswer}. You need {item_price - player_gold} more gold.")
    shop() # Return to shop menu     
    

def generateloot(numItems, itemList):
    
    # Loot generation depending on user input
    if itemList == "commonitems":
        loot_list = list(common_items.keys())
    elif itemList == "uncommonitems":
        loot_list = list(uncommon_items.keys())
    elif itemList == "rareitems":
        loot_list = list(rare_items.keys())
    else: # Error handling if no correct list is input 
        print("item list not found")
        return

    # loot Generation and Gold Generation, also telling the user their rewards
    random_loot = random.sample(loot_list, numItems)
    print("Congratulations you found:")
    print("-------------------------")
    
    for reward1 in random_loot:
        print(reward1)
    
    gold_loot = random.randint(3,18)  
    print("-------------------------")
    print("Added loot and " + str(gold_loot) + " gold to bag")
    print()
    
    # Add random loot gold to players bag
    global player_gold 
    player_gold = int(player_gold) + gold_loot
    player_bag.extend(random_loot)
      
login()
mainmenu()

#   "Function Testing"
#bag()
#lootgenerator()
#potionmaker()
#shop()
#shopPurchase()
