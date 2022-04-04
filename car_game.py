
#This is a car game without graphics.
command=""
started= False
while True:
    command = input(" > ").lower()
    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started ...")
    elif command == 'stop':
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped ...")
    elif command == 'help':
        print("""
Start - to start car
Stop - to stop car
Quit - to quit the game
    """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I'don't understand the command.")
    