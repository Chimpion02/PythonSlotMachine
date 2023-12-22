from slot_machine import SlotMachine, Player

def main():
    player = Player()
    slot_machine = SlotMachine()

    print("Welcome to the Slot Machine!")
    player.deposit()

    while True:
        print(f"Your current balance is ${player.balance}")
        if input("Press enter to play (q to quit): ").lower() == 'q':
            break

        bet, lines = player.get_bet()
        result = slot_machine.spin(bet, lines)
        player.balance += result
        print(f"Your new balance is ${player.balance}")

    print(f"You left with ${player.balance}.")

if __name__ == "__main__":
    main()
