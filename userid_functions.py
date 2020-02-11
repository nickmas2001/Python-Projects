#This program will create a login for a user, and check the password for several criteria
#By: Nick Mastrangelo
#Date: 10/31/2019
import re 
def createUserName ():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    return first [0] + last

def createPassword ():
    password = input("Please enter a password:")
    return password


def checkFirstCharacter (firstchar):
  if firstchar.isalpha():
    return True
  else:
    return False

def checkRemainingChars(remainingchars):
  if re.search("[0-9]", remainingchars):
    return True
  else:
    return False

def checkSpecialchars(specialChars):
  if not re.search("[!@#$%^&*?~]",specialChars):
    return False
  else:
    return True

def checkforbidchars(forbidchars):
  if re.search("[.]",forbidchars):
    return False
  elif re.search("[\s]", forbidchars):
    return False

def checkCharLength (charlength):
  for ch in charlength:
    if len(charlength) < 8:
      return False
  else:
    return True

def main ():
  # Prompts user for first and last name, and creates a username using first letter of first name + last name. Example: John Smith = jsmith
  username = createUserName ()
  print("Your username is:",username)

  # Prompts user to create a password
  valid = False
  while valid == False:
    password = createPassword ()
    #Checks first character of password for a letter
    if checkFirstCharacter(password[0]) == False:
      print("First character must have a letter.")
      valid = False

      #Checks remaining characters for numbers
    elif not checkRemainingChars(password):
      print("Password must be contain at least one number.")
      valid = False

      #Checks that character length is at least 8 characters
    elif checkCharLength(password) == False:
      print("Password must be 8 or more characters long")
      valid = False

      #Checks that password has at least one special character
    elif checkSpecialchars(password) == False:
      print("Please use one instance of: !,@,#,$,%,^,&,*,?")
      valid = False

    #Checks to make sure password does not have periods or spaces
    elif checkforbidchars(password) == False:
        print("You have used a forbidden character.")
        valid = False

    #If password meets all criteria, "password accepted" message will be printed out
    else:
      print("Password accepted.")
      valid = True
main()
