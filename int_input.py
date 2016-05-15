__author__ = "Patrick Shaw"


def int_input(message):
    while True:
        try:
            return int(input(message))
        except Exception:
            pass


def range_input(message, min, max):
    while True:
        value = int_input(message)
        if value < min:
            print("Must be greater than or equal to " + str(min))
            continue
        elif value >= max:
            print("Must be less than " + str(max))
            continue
        return value