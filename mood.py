#!/bin/env python3
"""
Fearghal's Mood Recorder (FMR) Version 1.0.0


This programs function is to record and log the mood of a person, and tell them a nice message is they are feeling bad or sad.
This program supports command line arguments, as well as just asking the user a question of how the user is feeling if no command line arguments are given.
The program will not record the user mood if the input for the mood is not an integer.
This program also has safe guards in place if the user inputs unsupported data into the program it self, or via a command line argument.


"""
__author__ = 'Fearghal Hayes'
__date__ = '10 September 2020'
__credits__ = 'Myself'
__version__ = '1.0.0'

import re
import datetime
import argparse
from time import sleep


def parse_command_line_args():  # This is the function that is required for the command line arguments to work.
    arg_description = "This is Fearghal's Mood Recorder"
    arg_parser = argparse.ArgumentParser(prog="FMR", description=arg_description)
    arg_parser.add_argument("--mood", "-m", action="store", dest="mood", type=int, required=False,
                            # This line adds the command line arguments to the function.
                            help="This the main argument to use with this program, "
                                 "after this argument input how you are feeling today "
                                 "on a scale from -5 to 5.")
    arguments = arg_parser.parse_args()
    return arguments  # Returns the value of the


delay = 0.1


def show_loading():
    print("Loading, Please wait (|)", end="\r", flush=True)
    sleep(delay)
    print("Loading, Please wait (/)", end="\r", flush=True)
    sleep(delay)
    print("Loading, Please wait (—)", end="\r", flush=True)
    sleep(delay)
    print("Loading, Please wait (\\)", end="\r", flush=True)
    sleep(delay)
    print("Loading, Please wait (—)", end="\r", flush=True)


def print_args_to_file():
    print("Date Recorded: ", date, "\n"
                                   "Time Recorded: ", time, "\n"
                                                            "Mood Recorded: ", args.mood, "\n", file=log
          )


def print_user_input():
    print("Date Recorded: ", date, "\n"
                                   "Time Recorded: ", time, "\n"
                                                            "Mood Recorded: ", user_input, "\n", file=log
          )


right_now = datetime.datetime.now()
date = right_now.strftime("%A, %d, %B, %Y")
time = right_now.strftime("%H:%M")
log = open("mood.log", "a")

if __name__ == "__main__":
    args = parse_command_line_args()
    if args.mood is not None:
        print("Hello, and welcome to Fearghal's Mood Recorder (FMR)")
        show_loading()
        show_loading()
        show_loading()
        if args.mood == 5:
            print("You're doing great!")
            print_args_to_file()
            log.close()
        if args.mood == 4:
            print("you are Looking good!")
            print_args_to_file()
            log.close()
        if args.mood == 3:
            print("you are Exellent!")
            print_args_to_file()
            log.close()
        if args.mood == 2:
            print("You're getting there")
            print_args_to_file()
            log.close()
        if args.mood == 1:
            print("Good to know")
            print_args_to_file()
            log.close()
        if args.mood == 0:
            print("Perfectly balanced, as all things should be...")
            print_args_to_file()
            log.close()
        if args.mood == -1:
            print("You're going to be ok")
            print_args_to_file()
            log.close()
        if args.mood == -2:
            print("There's always darkness before the dawn")
            print_args_to_file()
            log.close()
        if args.mood == -3:
            print("Hang in there!")
            print_args_to_file()
            log.close()
        if args.mood == -4:
            print("Sorry to hear that :(, things will get better!")
            print_args_to_file()
            log.close()
        if args.mood == -5:
            print("Keep your chin up!")
            print_args_to_file()
            log.close()
    elif args.mood is not None and args.mood < -5:
        print("Sorry, Please use the range '-5 to 5'")
    elif args.mood is not None and args.mood > 5:
        print("Sorry, Please use the range '-5 to 5'")

    elif args.mood is None:
        print("It seems you have given no command line arguments, "
              "would you like to exit the program and type an argument "
              "(A list of the arguments can be seen by typing '<NameOfPythonFile> -h'")

        ans = None
        while ans is None:
            ans = input("Yes [y], or No [N]\n").lower()
            if ans not in ['yes', 'y', 'Y', 'Yes', 'YES', 'yES', 'yeS', 'yEs', '', 'n', 'no', 'NO', 'nO', 'No']:
                print("Please enter Yes or No, nothing else")
                ans = None
            if ans in ['yes', 'y', 'Y', 'Yes', 'YES', 'yES', 'yeS', 'yEs']:
                print("Goodbye.")
                exit(0)

        if ans in ['', 'n', 'no', 'NO', 'nO', 'No']:
            show_loading()
            show_loading()
            print("Hello, and welcome to Fearghal's Mood Recorder (FMR)")
            user_input = input(
                "On a scale from -5 to 5 (-5 being very bad, and 5 being excellent), "
                "how would you rate your mood today?"
                "\n\n")
            show_loading()
            show_loading()

            if re.search('[0-9]', user_input) and user_input is not None:
                user_input = int(user_input)
                # The following line of code are checking for which value the user inputed for the question:

                if user_input < -5:
                    print("Sorry, Please use the range '-5 to 5'")
                if user_input > 5:
                    print("Sorry, Please use the range '-5 to 5'")

                if user_input == 5:
                    print("You're doing great!")
                    print_user_input()
                    log.close()
                if user_input == 4:
                    print("Looking good!")
                    print_user_input()
                    log.close()
                if user_input == 3:
                    print("Exellent!")
                    print_user_input()
                    log.close()
                if user_input == 2:
                    print("You're getting there")
                    print_user_input()
                    log.close()
                if user_input == 1:
                    print("Good to know")
                    print_user_input()
                    log.close()
                if user_input == 0:
                    print("Perfectly balanced, as all things should be...")
                    print_user_input()
                    log.close()
                if user_input == -1:
                    print("You're going to be ok")
                    print_user_input()
                    log.close()
                if user_input == -2:
                    print("There's always darkness before the dawn")
                    print_user_input()
                    log.close()
                if user_input == -3:
                    print("Hang in there!")
                    print_user_input()
                    log.close()
                if user_input == -4:
                    print("Sorry to hear that :(, things will get better!")
                    print_user_input()
                    log.close()
                if user_input == -5:
                    print("Keep your chin up!")
                    print_user_input()
                    log.close()

            else:
                print("Sorry, please only use numbers, nothing else.")
                exit(1)
