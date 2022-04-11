def gtn():
  import random
  
  #Set the "player" gamemode up.
  
  def player_guess(x):
    random_number = random.randint(1, x)
    player_guess = 0
    while player_guess != random_number:
      player_guess = int(input(f"Guess a whole number between 1 and {x}: "))
      if player_guess > random_number:
        print("Too high!")
      elif player_guess < random_number:
        print("Too low!")
    print(f"Congratulations! You guessed the correct number: {random_number}")
  
  #Set the "quesser" gamemode up.
  
  def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
      computer_guess = random.randint(low, high)
      feedback = input(f"Is the number {computer_guess} too high (H) or too low (L)?\n\n")
      if feedback == "L":
        low = computer_guess + 1
      elif feedback == "H":
        high = computer_guess - 1
      elif feedback != "L" and feedback != "H" and feedback != "C":
        print("Invalid feedback!")
        exit()
    print(f"Correct - The computer has guessed the correct number: {computer_guess}")
  
  #Ask the player what gamemode they want to play
  
  print("Number Guesser - v.0.2")
  print("Gamemode: 1 (You guess the number)\nGamemode: 2 (The computer guesses the number)")
  game_choice = input("Do you want to play as the player (1) or the quesser (2)?\n\n")
  
  #If user chooses to play as a player
  
  if game_choice == "1":
    x = input("INSTRUCTIONS: Choose the upper bound. The computer will generate a random whole number between 1 and that upper bound. Guess\nthat number:\n\n")
    player_guess(int(x))
  
  #If user chooses to play as a quesser
  
  elif game_choice == "2":
    print("INSTRUCTIONS: You will choose the upper bound and the secret\nnumber for the computer to guess. Enter 'H' if the computer's\nguess is too high, 'L' if it's too low and 'C' if it's correct.")
    x = input("Choose the upper bound:\n\n")
    computer_guess(int(x))
  
  else:
    print("Invalid gamemode!")
    exit()
