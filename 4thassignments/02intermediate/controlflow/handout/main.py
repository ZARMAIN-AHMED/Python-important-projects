import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0  # Track user’s correct guesses

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}:")
        user_number = random.randint(1, 100)  # User's number
        computer_number = random.randint(1, 100)  # Computer's number

        # Print the user's number
        print(f"Your number is {user_number}")
        
        # Ask the user whether they think their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Ensure valid input
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Game logic
        if guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Show score after each round
        print(f"Your score is now {score}")

    print("\nThanks for playing!")
    print(f"Your final score is {score}")

    # Conditional ending messages based on score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
