# Complete Code for Problem #1 and #2

def list_practice():
    # Problem #1: List Practice
    print("\n--- List Practice ---")
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print(f"Length of the list: {len(fruit_lst)}")
    
    # Add 'mango' at the end of the list
    fruit_lst.append('mango')
    
    # Print the updated list
    print("Updated fruit list:")
    for fruit in fruit_lst:
        print(fruit)

# --- Problem #2: Index Game Functions ---

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    # Problem #2: Index Game
    print("\n--- Index Game ---")
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print("Result:", access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Updated List:", modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced List:", slice_list(lst, start, end))
    else:
        print("Invalid operation.")

# --- Main Function ---
def main():
    list_practice()
    index_game()

if __name__ == '__main__':
    main()
