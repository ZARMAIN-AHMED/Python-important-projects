import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0  # Track user’s correct guesses

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}:")
        secret_number = random.randint(1, 100)

        while True:
            try:
                guess = int(input("Guess the number (between 1 and 100): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Correct! 🎉")
                score += 1
                break

    print("\nGame Over!")
    print(f"You guessed correctly {score} out of {NUM_ROUNDS} rounds.")

if __name__ == "__main__":
    main()
