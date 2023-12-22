import math
import random

MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def spin(balance, ROWS, COLS, symbol_count, symbol_value):
    print(f"Your balance is ${balance}")
    bet, lines = getBet(balance)
    total_bet = bet*lines
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
def get_slot_machine_spin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    #columns = get_slot_machine_spin(rows,cols,symbols)
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end ="")

        print()

def deposit():
    validAmount = False
    while validAmount == False:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                validAmount = True
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid input, please enter a number.")
    return amount

def lineFormat(lineUsed):
    format_line = "-"
    lineLen = len(lineUsed) * 1.1
    lineLen  = round(lineLen)
    for i in range(0, lineLen):
        format_line = format_line + str("-")
    print(format_line)
    print(f"  {lineUsed} ")
    print(format_line)


def getBet(balance):
    linesAmount = get_number_of_lines()
    print(f"You are betting on {linesAmount} lines.")
    print(f"Your current balance is ${balance}")
    highestAmount = balance/linesAmount
    highestAmount = math.floor(highestAmount)
    validInput = False
    while validInput == False:
        bettingInp = input(f"How much money would you like to bet on each line? ($1 - ${highestAmount}) $")
        if bettingInp.isdigit():
            bettingInp = int(bettingInp)
            if bettingInp >= 1 and bettingInp <= highestAmount:
                validInput = True
                show_info(balance,linesAmount,bettingInp)
            else:
                print(f"You do not have enough to bet that much. Amount must be between $1 - ${highestAmount}.")
        else:
            print("Please enter a valid number.")
    return bettingInp, linesAmount

def get_number_of_lines():
    validAmount = False
    while validAmount == False:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                validAmount = True
            else:
                print(f"Amount must be a valid number of lines. The maximum limit is {MAX_LINES}.")
        else:
            print("Invalid input, please enter a number.")
    return lines

def show_info(balance,lines,bet):
    lineFormat(f"Your balance is ${balance}")
    totalBet = lines * bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")
