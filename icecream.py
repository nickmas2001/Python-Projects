#Asks the user if they want hard or soft ice cream
def ice_cream():
  invalid = True
  while invalid == True:
    ice_cream = input("Would you like hard or soft serve?:").lower()
    if ice_cream == "hard":
      return ice_cream
      False
    elif ice_cream == "soft":
      return ice_cream
      False
    else:
      print("Please choose hard or soft.")
      True

#If the user chooses hard-serve, this function asks the user how many scoops they would like
def scoops():
  invalid = True
  while invalid == True:
    scoops = input("Would you like 1 or 2 scoops?:")
    if scoops == "1":
      return scoops
      invalid = False
    elif scoops == "2":
      return scoops
      invalid = False
    else:
      print("Please choose 1 or 2 scoops.")
      invalid = True

#If user chooses soft-serce, this function asks the user what size they would like
def size():
  invalid = True
  while invalid == True:
    size = input("Would you like small or large? (S/L):").lower()
    if size == "s":
      return size
      invalid= False
    elif size == "l":
      return size
      invalid= False
    else:
      print("Please choose small or large.")
      invalid= True

#This function asks the user if they would like sprinkles
def sprinkles():
  invalid = True
  while invalid == True:
    sprinkles = input("Would you like sprinkles? (Y/N):").lower()
    if sprinkles.lower() == "y":
      return sprinkles
      invalid = False
    elif sprinkles.lower() == "n":
      return sprinkles
      invalid = False
    else:
      print("Please choose yes or no.")
      invalid = True
    
#Main function
def main():
  
    price = 0 
    extras = 0
    
    print("Welcome to the ice cream shop!")
    serve_choice = ice_cream()
    
    #Calculates price based on serving size, and toppings
    if serve_choice == "hard":
      hard_scoops = scoops()
      if hard_scoops == "1":
        price = price + 1.00
      elif hard_scoops == "2":
        price = price + 1.50
      sprinkle_choice = sprinkles()
      if sprinkle_choice == "y":
        extras = extras + 0.10
      elif sprinkle_choice == "n":
        extras = 0

    #Calculates price based on serving size, and toppings
    elif serve_choice == "soft":
      soft_size = size()
      if soft_size == "s":
        price = price + 1.25
      elif soft_size == "l":
        price = price + 1.75
      sprinkle_choice = sprinkles()
      if sprinkle_choice == "y":
        extras = extras + 0.10
      elif sprinkle_choice == "n":
        extras = 0
    
    #Calculates total amount and prints to user
    total = price + extras 
    print("Your total is: $",total,". Enjoy!")
main()

