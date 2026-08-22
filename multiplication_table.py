def get_number():
    while True:
        n = input("Enter a number to see its times table: ")
        try:
            n = int(n)
            return n
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue


get_number()
