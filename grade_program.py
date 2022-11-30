#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Nov 28, 2022
# A program using functions to find a input grade percentaged.

# Second function with a switch case inside
# to display which level has what percentage
def calc_mark(level):
    match level:
        case "4+":
            return 98
        case "4":
            return 91
        case "4-":
            return 83
        case "3+":
            return 78
        case "3":
            return 75
        case "3-":
            return 71
        case "2+":
            return 68
        case "2":
            return 65
        case "2-":
            return 61
        case "1+":
            return 58
        case "1":
            return 55
        case "1-":
            return 51

        # Case for invalid input
        case _:
            return -1


def main():

    # user input
    user_input = input("Enter a grade level R-4 (3+): ")

    # Call back to first function
    user_level = calc_mark(user_input)

    # Checks for invalid inputs
    if user_level == -1:
        print(f" {user_input} is not a valid input")

    # Display outcome
    elif user_level != -1:
        print(f"{user_input} has the middle percentage of {user_level}")


if __name__ == "__main__":
    main()
