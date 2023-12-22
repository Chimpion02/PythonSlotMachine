import tkinter as tk
from tkinter import messagebox
import random
import math


class SlotMachine:
    ROWS = 3
    COLS = 3
    MAX_LINES = 3
    SYMBOL_COUNT = {"A": 3, "B": 4, "C": 6, "D": 8}
    SYMBOL_VALUE = {"A": 5000, "B": 300, "C": 10, "D": 3}

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
    def check_winnings(columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            if all(symbol == column[line] for column in columns):
                winnings += SlotMachine.SYMBOL_VALUE[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines


class Player:
    def __init__(self, balance=0):
        self.balance = balance


class SlotMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")
        self.root.geometry("400x400")  # Adjusted for new deposit box

        self.player = Player()
        self.slot_machine = SlotMachine()

        self.balance_label = tk.Label(root, text=f"Balance: ${self.player.balance}")
        self.balance_label.pack(pady=10)

        self.spin_result_label = tk.Label(root, text="")
        self.spin_result_label.pack(pady=10)

        bet_label = tk.Label(root, text="Bet Amount:")
        bet_label.pack()
        self.bet_entry = tk.Entry(root)
        self.bet_entry.pack(pady=5)

        lines_label = tk.Label(root, text="Number of Lines:")
        lines_label.pack()
        self.line_entry = tk.Entry(root)
        self.line_entry.pack(pady=5)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin)
        self.spin_button.pack(pady=10)

        deposit_label = tk.Label(root, text="Deposit Amount:")
        deposit_label.pack()
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)

    def spin(self):
        try:
            bet = int(self.bet_entry.get())
            lines = int(self.line_entry.get())

            if bet <= 0 or lines <= 0 or bet * lines > self.player.balance:
                raise ValueError("Check your bet and lines. Ensure sufficient balance.")
            if lines > SlotMachine.MAX_LINES:
                raise ValueError(f"Maximum {SlotMachine.MAX_LINES} lines allowed.")

            columns = self.slot_machine.get_slot_machine_spin()
            winnings, winning_lines = self.slot_machine.check_winnings(columns, lines, bet)
            self.player.balance += winnings - (bet * lines)
            self.update_balance_label()
            self.update_spin_result(columns, winnings, winning_lines)
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))

    def deposit(self):
        try:
            amount = int(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.player.balance += amount
            self.update_balance_label()
            self.deposit_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid deposit amount.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.player.balance}")

    def update_spin_result(self, columns, winnings, winning_lines):
        result_text = "Spin Result:\n"
        for row in range(SlotMachine.ROWS):
            for col in columns:
                result_text += col[row] + " "
            result_text += "\n"
        result_text += f"\nYou won: ${winnings}\n"
        result_text += "Winning lines: " + ", ".join(map(str, winning_lines)) if winning_lines else "No winning lines"
        self.spin_result_label.config(text=result_text)


def main():
    root = tk.Tk()
    gui = SlotMachineGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
