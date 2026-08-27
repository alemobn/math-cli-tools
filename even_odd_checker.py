def get_number():
    while True:
        n = input("Enter a number to check if it's even or odd. ")
        try:
            n = int(n)
            return n
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue


def is_even(n):
    return n % 2 == 0


number = get_number()

if is_even(number):
    print("Even!")
else:
    print("Odd!")
