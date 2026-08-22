def get_number():
    while True:
        n = input("Enter a number to see its times table: ")
        try:
            n = int(n)
            return n
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue


def display_table(n):
    print(f"\n----- Table of {n} -----")
    for multiplier in range(1, 11):
        print(f"{n} x {multiplier} = {n * multiplier}")
    print("----------------------")


number = get_number()
display_table(number)
