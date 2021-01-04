# command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('car is already started!')
        else:
            started = True
            print('car started..ready to go!')

    elif command == "stop":
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car Stopped')

    elif command == "quit":
        print('game quited')
        break
    else:
        print("Sorry, I don't understand")
