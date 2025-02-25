import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


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



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
    

def deposit():
    while True:
        amount = input("Enter your number you wanna deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount  # Corrected placement of return statement
            else:
                print("Enter a number greater than 0")
        else:
            print("Please enter a valid number")


def get_no_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a number between 1 and", MAX_LINES)
        else:
            print("Please enter a valid number")


def get_bet():
    while True:
        amount = input("what would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(
                    f"Enter a number greater than ${MIN_BET} - ${MAX_LINES} ")
        else:
            print("Please enter a valid number")


def spin(balance):
    lines = get_no_of_lines()

    while True:
         bet = get_bet()
         total_bet = bet * lines

         if total_bet > balance:
             print(
             f"you do not have sufficient amont to bet,you current balance is {balance}")
         else:
             break

    print(f"you are betting ${bet} on {lines} lines. total bet is ${total_bet}.")
    slots =  get_slot_machine_spin(ROWS,COLS,SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_COUNT)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()

