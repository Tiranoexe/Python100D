from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = randint(1,100)
print(f"Pssst the actual number is {number}")

difficulty = input("Choose a difficulty. Type 'easy' of 'hard': ")
if difficulty == 'easy':
  attempts = 10
elif difficulty == 'hard':
  attempts = 5

keep_guessing = True
while attempts > 0 and keep_guessing:
  print(f"You have {attempts} remaining to guess the number")
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
    keep_guessing = False
  elif guess > number:
    print("Too high")
    attempts -= 1
  elif guess < number:
    print("Too low")
    attempts -= 1

if attempts == 0:
  print("You've run out of guesses, you lose.")
