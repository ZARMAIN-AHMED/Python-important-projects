def main():
    lst = [ "apple, mango, banana"]  

    val = input("Enter a value: ")  
    while val:  
        lst.append(val) 
        val = input("Enter a value: ")  

    print("Here's the list:", lst)




if __name__ == '__main__':
    main()