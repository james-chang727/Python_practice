# Description:
# This program uses the Coin class to create a list of coins. The program calculates the percentage 
# of heads and tails and prints the results.

from coin_module import Coin


def print_menu():
    while True:
        print("Type:")
        print("\tf - to flip the coin")
        print("\tq - to quit")

        select = input("Enter Selection:")

        if select == 'f':
            print(f'The result was {Coin()}\n')
        elif select == 'q':
            break
        else:
            raise ValueError('Wrong Entry! Try Again!')


def main():
    print_menu()
    print("\nBye, Bye!\n")
        

if __name__ == "__main__":
    main()

