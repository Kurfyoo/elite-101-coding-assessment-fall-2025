import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(clr=True):
    print()
    key = input("PRESS ENTER TO CONTINUE (OR TYPE 'exit' TO QUIT): ")
    if key.strip().lower() == "exit":
        sys.exit(0)

    while key != "":
        print("invalid input.")
        key = input("PRESS ENTER TO CONTINUE (OR TYPE 'exit' TO QUIT): ")
        if key.strip().lower() == "exit":
            sys.exit(0)
    if clr:
        clear()

def pause(seconds):
    time.sleep(seconds)
