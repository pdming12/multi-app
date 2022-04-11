#Import libraries

from guessthenumber import gtn
from calculator import calculator
from rockpaperscissors import rps

def password_inquiry(): #the function that inquires the password from the user
  password_prompt = input("Enter the password:\n\n")

  trys = 4
  if password_prompt == password:
    print("Welcome!\n")
    
  else:
    print(f"Wrong! You have {trys} attempts left.")
    while trys > 0 and password_prompt != password:
      password_prompt = input("Enter the password:\n\n")
      if password_prompt != password:
        trys = trys - 1
        print(f"Wrong! You have {trys} attempts left.")
      else:
        print("Welcome!")
    if trys == 0:
      print("Out of attempt!")
      exit()
#Ask the user to set a password
print("Set a new password. Your password needs to contain\nat least 8 letters.\n")
password = input("Enter your password: ")
password_confirm = input("Re-enter your password: ")

#Check/Require that the password must contain at least 8 letters
while len(password) < 8:
  if len(password) < 8:
    print("\nYour password needs to be at least 8 letters.\n")
    password = input("Enter your password: ")
    password_confirm = input("Re-enter your password: ")

while password != password_confirm: #If the re-entered password = the set password
  print("\nYour confirming password is not the same as the password you set. Try again.\n")
  password_confirm = input("Re-enter your password: ")

#When the user successfully creates a password
print(f"Your password has been set to {password}!")

#THE ACTUAL PROGRAM
print("\nThere are currently 3 apps in our library.")
app_choice = input("\nCalculator (1), Rock-Paper-Scissors (2) or Guess The Number (3)?\n")

if app_choice == "1": #the user chooses to run the calculator
  
  password_inquiry() #requires the password
  calculator() #run the calculator
  
elif app_choice == "2": #the user chooses to run the game "rock-paper-scissors"

  password_inquiry()
  rps() #runs the game

  #ask if the user wants to continue playing
  continue_prompt = input("\nDo you want to continue playing?\n(Y) for Yes, (N) for No\n\n")
  while continue_prompt != "Y" and continue_prompt != "N":
    continue_prompt = input("Invalid choice!\n(Y) for Yes, (N) for No\n\n")
  while continue_prompt == "Y":
    rps()
    continue_prompt = input("\nDo you want to continue playing?\n(Y) for Yes, (N) for No\n\n")
  if continue_prompt == "N":
    exit()
    
elif app_choice == "3":
  password_inquiry()
  gtn() #run guess the number

  #ask if the user wants to continue
  continue_prompt = input("\nDo you want to continue playing?\n(Y) for Yes, (N) for No\n\n")
  while continue_prompt != "Y" and continue_prompt != "N":
    continue_prompt = input("Invalid choice!\n(Y) for Yes, (N) for No\n\n")
  while continue_prompt == "Y":
    gtn()
    continue_prompt = input("\nDo you want to continue playing?\n(Y) for Yes, (N) for No\n\n")
  if continue_prompt == "N":
    exit()
