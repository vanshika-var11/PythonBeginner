
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
#Function to check user guess against the number
def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess,returns the number of turns left."""
    if user_guess>actual_answer:
        print("Your guess is too high")
        return turns - 1
    elif user_guess<actual_answer:
        print("Your guess is too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

#Function to set difficulty
def set_difficulty():
    level=input("Choose your difficulty.Type 'easy or 'hard':")
    if level=='easy':
       return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
#Choosing a  random no. btw 1 to 100
   print("Welcome to Number Guessing Game!")
   print("Im thinking of a number between 1 and 100!")
   answer=randint(1,100)
   print(f"Pass, the correct answer is {answer}")


   turns=set_difficulty()

   guess=0
   while guess!=answer:
     print(f"You have {turns} guesses left.")
#Let the user guess a number
     guess=int(input("Make a guess:"))
     turns=check_answer(guess, answer,turns)
    if  turns==0:
        print("You run out of guesses You lose!")
        return
    elif guess!=answer:
        print("Guess again")

game()

#Track the guessing functionality if they get it wrong