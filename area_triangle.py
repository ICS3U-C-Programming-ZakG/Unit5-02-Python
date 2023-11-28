#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 28, 2023
# This program calculates the area of a triangle.


def calc_area(base, height):
    # calculate area
    area = base * height / 2

    # display area
    print(
        "The area of a triangle with a height of {:.2f} and a base of {:.2f} is {:.2f}cm^2".format(
            height, base, area
        )
    )


def main():
    # introduce program to the user
    print("Hello, this program calculates the area of a triangle.\n")

    # get user inputs
    user_base = input("Please enter a base: ")
    user_height = input("Please enter a height: ")
    print()

    # try converting input to float
    try:
        user_base_int = float(user_base)

        # try converting second input to float
        try:
            user_height_int = float(user_height)

            # check if numbers are greater than zero
            if (user_base_int > 0) and (user_height_int > 0):
                # call function
                calc_area(user_base_int, user_height_int)

            # tell user no negatives
            else:
                print("You must input numbers greater than zero.")

        # catch invalid inputs
        except Exception:
            print("{} is not a positive number.".format(user_height))

    # catch invalid inputs
    except Exception:
        print("{} is not a positive number.".format(user_base))


if __name__ == "__main__":
    main()
