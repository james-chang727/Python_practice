
from dice_module import Dice


def print_menu():
    while True:
        print("Type:")
        print("\tt - to cast the dice")
        print("\tq - to quit")

        select = input("Enter Selection:")

        if select == 't':
            print(f'The result was {Dice()}\n')
        elif select == 'q':
            break
        else:
            raise ValueError('Wrong Entry! Try Again!')


def main():
    print_menu()
    print("\nBye, Bye!\n")


if __name__ == "__main__":
    main()