from SlotMachineFunctions import deposit, lineFormat, spin
from SlotMachineFunctions import ROWS, COLS, symbol_count, symbol_value
#from SlotMachineFunctions import *
def main():
    balance = 0
    lineFormat("Welcome to the slot machine!")
    print("")
    balance += deposit()
    playing = True
    while playing == True:
        lineFormat(f"Your current balance is ${balance}")
        answer = input("Press enter to play (q to quit): ")
        if answer == "q":
            playing = False
        else:
          balance += spin(balance, ROWS, COLS, symbol_count, symbol_value)

    lineFormat(f"You left with ${balance}.")

if __name__ == "__main__":
    main()
