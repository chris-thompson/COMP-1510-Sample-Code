def square(number):
    """
    Return the square of number.

    :param number: a squarable number
    :precondition: number is a real number
    :postcondition: calculates the square of number
    :return square: the square of number

    >>> square(3)
    9
    >>> square(-3)
    9
    >>> square(0)
    0
    """
    return number * number


def main():
    print("The square of 2 is", square(2))


if __name__ == "__main__":
    main()
