# new try/arrangement of previous class
# command = ""
started = True

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('car started..ready to go!')
        else:
            started = False
            print('car is already started!')

    elif command == "stop":
        if started:
            print('Car Stopped')

        else:
            started = False
            print('Car is already stopped!')

    elif command == "quit":
        print('game quited')
        break
    else:
        print("Sorry, I don't understand")
