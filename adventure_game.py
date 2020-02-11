#final_project.py
#By: Nick Mastrangelo
#Date: 12/6/2019
#Introduction to Programming- Final Project

#This is a text-based adventure game where the user is stranded in the woods and has to find their way out.

#This function will ask the user if they want to play again
def play_again ():
  while True:
    play_again = input("Would you like to play again? (Y/N):")
    if play_again.lower() == "y":
      return play_again
      True
    elif play_again.lower() == "n":
      print("Thanks for playing!")
      return play_again
      True
    else:
      print("Please enter a valid selection.")
      False

#This function will prompt the user for their initial choice
def choice0 ():
  while True:
    choice0 = input("There are three paths. Would you like to go left, right, or straight? (L/R/S):")
    if choice0.lower() == "l":
      True
      return choice0
    elif choice0.lower() == "r":
      True
      return choice0
    elif choice0.lower() == "s":
      True
      return choice0
    else:
      print("Please enter a valid selection")
      False

#This function will be called if user chooses the left path
def choice1():
  while True:
    choice1 = input("You have come across another split in the trail. Do you go left or right? (L/R):")
    if choice1.lower() == "l":
      True
      return choice1
    elif choice1.lower() == "r":
      True
      return choice1
    else:
      print("Please enter a valid selection")
      False

#This function will be called if user chooses the straight path
def choice2():
  while True:
      choice2 = input("You have come across another split in the trail. Do you go left or right? (L/R):")
      if choice2.lower() == "l":
        True
        return choice2
      elif choice2.lower() == "r":
        True
        return choice2
      else:
        print("Please enter a valid selection")
        False

#This function will be called if the user chooses the right path
def choice3():
  while True:
    choice3 = input("You have come across another split in the trail. Do you go left or right? (L/R):")
    if choice3.lower() == "l":
      True
      return choice3
    elif choice3.lower() == "r":
      True
      return choice3
    else:
      print("Please enter a valid selection")
      False
#This function will be called if user chooses left, left
def choice1a():
  print("After walking for hours, you get too tired to continue. You have not anything to eat or drink. You are severely dehydrated and are unable to continue. Game over.")
#This function will be called if user chooses left, right
def choice1b():
  print("As you walk down the trail. You see a silhouette in the distance. Curiously, you walk towards it. As you approach, you realize it is a black bear. The bear chases and attacks you. Game over.")

#This function is called if user chooses straight, left
def choice2a():
  print("After trekking through the frigid-cold weather, hypothermia sets in. You are unable to continue. Game over.")

#This function is called if user chooses straight, right
def choice2b():
  print("You have found the way out! Congratulations, you have escaped!")

#This function will be called if user chooses right, left
def choice3a():
  print("As you are walking, you feel a sharp pain in your thigh. You look down to realize that a rattlesnake has sunk its fangs into your leg. You start to feel woozy as you black out and fall to the ground. Game over.")

#This function will be called if user chooses right, right
def choice3b():
  print("You trip on a jagged branch. You fall over, breaking your leg on the branch. You scream for help, but nobody can hear your cries. Game over.")

#Main function
def main():
  restart = True
  while restart == True:
    print("You are lost in the woods in the middle of the night. You must find your way out. Good luck.")

    intital_choice = choice0()

    #If user chooses the left path:
    if intital_choice.lower() == "l":
      left = choice1()

      #If user chooses to go left at the second path:
      if left.lower() == "l":
        choice1a()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True

      #If user chooses the go right at the second path:
      elif left.lower() == "r":
        choice1b()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True
    #If the user chooses the straight path:
    elif intital_choice.lower() == "s":
      straight = choice2()

      #If user chooses to go left at the second path:
      if straight.lower() == "l":
        choice2a()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True

      #If user chooses the go right at the second path:
      elif straight.lower() == "r":
        choice2b()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True

    #If the user chooses the right path:
    elif intital_choice.lower() == "r":
      right = choice3()

      #If user chooses to go left at the second path:
      if right.lower() == "l":
        choice3a()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True

      #If user chooses the go right at the second path:
      elif right.lower() == "r":
        choice3b()
        play_again1 = play_again()
        if play_again1.lower() == "n":
          restart = False
        else:
          restart = True
main()
