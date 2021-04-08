command = ""
started = input("Enter true or false = ").title()
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Already started!")
        else:
            print("Started")
    elif command == "stop":
        if not started:
            print("Already stopped!")
        else:
            print("stopped")    
    elif command == "help":
        print("""
              start-to start
              stop- to stop
            """)
        break
else:
    print("Something is wrong")
