#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program uses a for loop
#   with user input


def main():
    # this function uses a for loop
    counter = 0
    odd = 0
    even = 0

    # input
    number_str = input("How many numbers do you want to add: ")
    print("")

    # process & output
    try:
        number_int = int(number_str)
        for counter in range(number_int):
            second_str = input("Enter the number: ")
            print("")
            second_int = int(second_str)
            if second_int % 2 == 0:
                even = even + second_int
            else:
                odd = odd + second_int
        print("The sum of all even numbers is = {0}.".format(even))
        print("The sum of all odd numbers is = {0}.".format(odd))

    except Exception:
        print("Oops invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
