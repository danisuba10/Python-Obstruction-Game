from src.service.ComputerPlayer import ComputerStupid, ComputerMiniMax
from src.ui.ui import UI

if __name__ == "__main__":
    run = True
    while (run):
        print("Should the opponent moves be random or should it use the Min-Max algorithm?\na.) Random\nb.) Min-Max\n")
        choice = input(">>>")
        if (choice.lower() == "a"):
            ui = UI(6, ComputerStupid)
            ui.menu()
            run = False
        elif (choice.lower() == "b"):
            ui = UI(6, ComputerMiniMax)
            ui.menu()
            run = False
        else:
            print("Wrong input!")