""" generator.py generates a list from an input list """

import argparse
import sys


def parse_duplicates_arguments(args):
    """ Parses the arguments provided on the command-line """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--verbose", help="Verbose mode", action="store_true")
    parser.add_argument('--list', nargs='+', type=str)

    arguments = parser.parse_args(args)
    return arguments, parser


def display_welcome_message():
    """ Display a welcome message """
    print("Generator generates a lists of lists from an input list!")
    print()


def display_list_of_lists(list_of_lists):
    """ Displays the list of lists """


def generate(starting_list):
    """ Assumes that starting_ is a list.
        Removes any element from list_one that also occurs in list_two """
    list_of_lists = []
    return list_of_lists


if __name__ == '__main__':
    display_welcome_message()
    # parse the arguments
    arguments, parser = parse_duplicates_arguments(sys.argv[1:])
    if arguments.verbose:
        print(arguments)
    # generate the required data
    if arguments.list is not None:
        list_of_lists = generate(arguments.list)
        print("Generating the List:")
        print()
        print("Length of Generated List:", len(list_of_lists))
        print()
        print("Generated List:")
        print()
        display_list_of_lists(list_of_lists)
        print()
