from game_data import data
from art import logo, vs
import random
from replit import clear

print(logo)
  
def create_person(account): 
  """Takes the account data and returns the printable format"""
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

score = 0
account_b = random.choice(data)
guess_right = True

while guess_right:

  
  
  account_a = account_b 
  account_b = random.choice(data)
  while account_b == account_a:
    account_b = random.choice(data)

  
  print(f"Compare A: {create_person(account_a)}.")
  print(vs)
  print(f"Against B: {create_person(account_b)}.")
  
  guess = input("Who has more followers? 'A' or 'B': ").lower()

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    guess_right = False
