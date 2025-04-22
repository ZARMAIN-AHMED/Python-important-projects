import random 
print("Welcome to the Number Guessing Game!") 
print("Guess a number between 50 and 100.") 
print("You have 5 attempts.") 
print("Let's start!") 


number_to_guess = random.randrange(50, 101) 

max_attempts = 5 

attempts_taken = 0 


while attempts_taken < max_attempts:
    
    attempts_taken += 1 
    user_guess = int(input("Please enter your guess: "))
 
    if user_guess == number_to_guess:
        print(
            f"The number is {number_to_guess} and you found it right!! in the {attempts_taken} attempt"
        ) 
        break 

    
    elif attempts_taken >= max_attempts and user_guess != number_to_guess:
        print(f"Oops sorry, the number is {number_to_guess} better luck next time!") 

   
    elif user_guess > number_to_guess:
        print("your guess is very high, try again!") 

    elif user_guess < number_to_guess:
        print("your guess is very low, try again!") 