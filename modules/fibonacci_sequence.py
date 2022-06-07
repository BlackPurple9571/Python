#!/usr/bin/env python
# Description: "Small script to calculate the Fibonacci number up to a certain
#   position or at a certain position. (https://en.wikipedia.org/wiki/Fibonacci_number)"

import argparse  # pip install argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pos", required=True, type=int, help="Position of the Fibonacci number to be calculated or "
                                                               "the position up to which the Fibonacci sequence is to "
                                                               "be calculated.")
    parser.add_argument("--list", type=bool, help="Create a list of all Fibonacci numbers in the selected range.")
    args = parser.parse_args()

    if args.pos and args.list is None:
        print("The Fibonacci number at the " + str(args.pos) + ". position is \"" + str(fib(args.pos)[-1]) + "\".")
    elif args.list is True:
        print("Below is a list of all Fibonacci numbers up to the " + str(args.pos) + " Fibonacci number.\n")

        fl = fib(args.pos)
        i = 0
        for num in fl:
            i += 1
            print(str(i) + ": \"" + str(num) + "\"")


def fib(r):
    fib_sequence = [1, 1]
    pointer = 0

    for i in range(r - 2):
        fib_sequence.append(fib_sequence[pointer] + fib_sequence[pointer + 1])
        pointer += 1

    return fib_sequence


if __name__ == "__main__":
    main()
