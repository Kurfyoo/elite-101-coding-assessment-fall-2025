import os
import sys
import time

def clear():
    os.system('clear')

def wait(clr=True):
    print()
    key = input("PRESS ENTER TO CONTINUE: ")
    if key == "exit_case":
        exit()
    while key != "":
        print("INVALID KEY")
        key = input("PRESS ENTER TO CONTINUE: ")
        if key == "exit_case":
            exit()
    if clr:
        clear()

def exit():
    print()
    print("Exiting the program.")
    sys.exit()

def pause(seconds):
    time.sleep(seconds)
