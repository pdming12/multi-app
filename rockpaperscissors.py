def rps():
  import random
  
  def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
      return True
    elif (player == "r" and opponent == "p") or (player == "p" and opponent == "s") or (player == "s" and opponent == "r"):
      return False
  
  def play():
    user = input("Rock (r), paper (p) or scissors (s)? \n\n")
    choices = ["r", "p", "s"]
    computer = random.choice(choices)
    while user not in choices:
      print("Invalid choice! Try again!")
      user = input("Rock (r), paper (p) or scissors (s)? \n\n")
    if user == computer:
      print(f"The computer chooses {computer}!")
      print("=> Draw!")
    if is_win(user, computer):
      print(f"The computer chooses {computer}!")
      print("=> You win!")
    elif is_win(computer, user):
      print(f"The computer chooses {computer}!")
      print("=> You lose!")
  
  print("Game: Rock - Paper - Scissors")
  print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors!")
  
  play()
