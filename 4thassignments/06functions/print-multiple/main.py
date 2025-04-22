def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
