import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
   
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]

    print("Generated Numbers:", numbers)

    total = sum(numbers)
    average = total / N_NUMBERS
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

if __name__ == '__main__':
    main()
