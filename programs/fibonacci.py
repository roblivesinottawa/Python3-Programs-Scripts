def main():
    user_input = int(input("Please, enter the number of terms: >>> "))
    

    n1, n2 = 0, 1
    count = 0

    if user_input <= 0:
        print("Enter a positive integer.")
    elif user_input == 1:
        print(f"Fibonnaci sequence up to {user_input}: ")
    else:
        print("Fibonnaci Series: ")
        while count < user_input:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
main()