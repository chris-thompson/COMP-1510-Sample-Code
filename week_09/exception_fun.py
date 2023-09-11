"""
Let's play with exceptions!
"""
import math


def function_can_throw(number):
    if type(number) is not int or number < 0:
        raise ValueError("I can only process positive integers!")
    else:
        return math.factorial(number)


def main():
    """
    The main function is the program that uses functions we write!
    """
    try:
        product = function_can_throw("a")
    except ValueError as e:
        print(e)
    else:
        print(product)
    finally:
        print("This always happens!")


if __name__ == "__main__":
    main()
