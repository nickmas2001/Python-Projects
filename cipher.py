#cipher.py
#Intro to Programming- Final Exam
#By: Nick Mastrangelo
#Date: 12/10/2019

#This program will encrypt the user's input using a Caesar cipher


MAX_DISPLACEMENT_SIZE = 26

def getWord():
    #Ask user for word to encrypt
      while True:
          word = str(input("Please enter the word you wish to encrypt (Letters only) :"))
          if word.isalpha():
              return word 
              True
          else:
              print("Error: Please use letters only.")
              False


def getDisplacement_value():
    #Ask user for displacement value
    displacement_value = 0 
    while True:
        displacement_value = int(input("Please enter a displacement value between 1-26:"))
        if (displacement_value >= 1 and displacement_value <= MAX_DISPLACEMENT_SIZE):
            return displacement_value
            True
        else:
            print("Error: Displacement value can only be between 1-26.")
            False

def encrypt(word,displacement_value):
    #Empty list for the encrypted word
    encryptedWord = ""
    #Converts each letter using the user's word and displacement value
    for symbol in word:
        if symbol.isalpha():
            num = ord(symbol)
            num += displacement_value

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedWord += chr(num)
            
    #Return the value of the encrypted word to the empty list
    return encryptedWord

def main():
    #Print welcome message
    print("Welcome to the Caesar Cipher Encrypter!")
    word = getWord()
    displacement_value = getDisplacement_value()
    
    #Print encrypted word 
    print("The encrypted word is:",encrypt(word, displacement_value))
   
   #Prompt user to press Enter to quit
    input("Press <Enter> to Quit.")
    
main()
    
    
    
   
            