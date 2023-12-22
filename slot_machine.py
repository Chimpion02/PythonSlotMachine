import random
import math

class SlotMachine:
    ROWS = 3
    COLS = 3
    MAX_LINES = 3
    SYMBOL_COUNT = {"A": 3, "B": 4, "C": 6, "D": 8}
    SYMBOL_VALUE = {"A": 5, "B": 4, "C": 3, "D": 2}

    @staticmethod
    def spin(player_bet, lines):
        print(f"Spinning the Slot Machine...")
        total_bet = player_bet * lines
        slots = SlotMachine.get_slot_machine_spin()
        SlotMachine.print_slot_machine(slots)
        winnings, winning_lines = SlotMachine.check_winnings(slots, lines, player_bet)
        print(f"You won ${winnings}.")
        print(f"You won on lines:", *winning_lines)
        return winnings - total_bet

    @staticmethod
    def get_slot_machine_spin():
        all_symbols = [symbol for symbol, count in SlotMachine.SYMBOL_COUNT.items() for _ in range(count)]
        columns = []

        for _ in range(SlotMachine.COLS):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(SlotMachine.ROWS):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)

        return columns

    @staticmethod
    def print_slot_machine(columns):
        for row in range(SlotMachine.ROWS):
            for i, column in enumerate(columns):
                if i != SlotMachine.COLS - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")
            print()

    @staticmethod
    def check_winnings(columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                if symbol != column[line]:
                    break
            else:
                winnings += SlotMachine.SYMBOL_VALUE[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines


class Player:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        while True:
            amount = input("How much do you want to deposit? $")
            if amount.isdigit() and int(amount) > 0:
                self.balance += int(amount)
                break
            else:
                print("Invalid input, please enter a positive number.")

    def get_bet(self):
        lines = self.get_number_of_lines()
        highest_amount = math.floor(self.balance / lines)
        while True:
            bet = input(f"How much money would you like to bet on each line? ($1 - ${highest_amount}) $")
            if bet.isdigit() and 1 <= int(bet) <= highest_amount:
                return int(bet), lines
            else:
                print("Invalid input, please enter a number within the allowed range.")

    @staticmethod
    def get_number_of_lines():
        while True:
            lines = input(f"Enter the number of lines to bet on (1 - {SlotMachine.MAX_LINES}): ")
            if lines.isdigit() and 1 <= int(lines) <= SlotMachine.MAX_LINES:
                return int(lines)
            else:
                print("Invalid input, please enter a number within the allowed range.")
