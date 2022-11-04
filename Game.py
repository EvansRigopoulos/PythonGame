import random



def get_choices():
  options = ["rock","paper","scissors"]

  player_choice = input("Enter a choice(rock,paper,scissors)\n")
  
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}

  return choices 
  
def check_win(player,computer):
  print(f"You chose {player} ,computer chose {computer}")
  
  if player == computer:
    return "It's a tie"
    
  elif player == "rock" :
    if computer == "scissors":
     return "Rock smashes scissors.Player wins"
    else :
      return "Paper covers rock!You lose."
      
  elif player == "scissors": 
    if computer == "rock":
     return "Rock smashes scissors.You lose."
    else :
      return "Scissors cuts paper!You win!"  
      
  elif player == "paper" :
    if computer == "scissors":
     return "Scissors cuts papers.You lose"
    else :
      return "Paper covers rock!You win."
      
choices = get_choices()

result = check_win(choices["player"],choices["computer"])

print(result)
