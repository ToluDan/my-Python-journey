import random 
from art import logo
from replit import clear
def deal_card():
 cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
 card=random.choice(cards)
 return card 
  


def play_game():
  print(logo)
  user_card=[]
  computer_card=[]
  game_over=False
  
  
  def  compare(user_score, computer_score):
    
    if user_score==computer_score:
     return "draw"
    elif computer_score==0:
     return "you lose! Your opponent has a Black Jack 😬"
    elif user_score==0:
      return "You win with a Black Jack!"
    elif user_score>21: 
      return "Oop! You went overboard this time so you lose"
    elif computer_score>21:
      return "You win!your opponent went overboard😆"
    elif user_score>computer_score:
      return "You win👍"
    else:
      return "You lose"
  
  
    
  def calculate_score(cards):
   total_score=sum(cards)
   return total_score
   if sum(cards)==21 and len(cards)==2:
    return 0
   if sum(cards)>21 and 11 in cards:
     cards.remove(11)
     cards.append(1)
  
  
     
  for _ in range(2):
   
   user_card.append(deal_card())
   computer_card.append(deal_card())
  
  
  while not game_over:
  
  
  
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card) 
    print(f"your card is:{user_card},your score is {user_score}, computer card is {computer_card[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      game_over=True
    else:
      option= input("Type y to get another card or n to pass")
      if option=="y":
       user_card.append(deal_card())
      else:
        game_over=True
  
  #to let computer play and keep drawing cards as long as it is less than 17 and aslo stops when it draws a black jack
  
  while computer_score!=0 and computer_score<17:
    computer_card.append(deal_card())
    computer_score=calculate_score(computer_card)
  
  
  
  print(f"your final hand is {user_card}, your score is {user_score}")
  
  print(f"computer hand is {computer_card}, computer score is {computer_score}")
  print(compare(user_score, computer_score))

while  input("Do you want to play a game of BlackJack?Type yes or no ")=="yes":
    clear()
    play_game()
