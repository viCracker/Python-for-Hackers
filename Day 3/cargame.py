# This should have been a car game, but I am a H4CKER
import time

print("Welcome To Cracker Tool")
command = 2
attack_status = 0
while command != 0:
    command = input("cracker_$ ")
    if command.lower() == "start":
        time.sleep(3)
        print("Attack started...")
        command = input("cracker_$ ")
        attack_status = 1
        while attack_status == int(1):
            if command.lower() == "stop":
                print("Clearing Tracks...")
                time.sleep(3)
                print("Attack Stopped Successfully")
                attack_status = 0
            elif command.lower == "help":
                print("try 'stop' command")
                attack_status = 1
                command = input("cracker_$ ")
            else:
                time.sleep(3)
                print("Command not supported see 'help'")
                attack_status = 1
                command = input("cracker_$ ")
    elif command.lower() == "help":
        print("\nstart -\tstarts attack on target\nstop - \tstops an ongoing attack\nquit - \tclose the program\n")
        command = 2
    elif command.lower() == "quit":
        print("Clearing Your Tracks...")
        time.sleep(3)
        print("Goodbye!")
        break
    else:
        print("Command Not Found, Try 'help'")
        command = 2
