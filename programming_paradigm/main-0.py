import sys
from bank_account import BankAccount

def parse_arg(arg: str):
    parts = arg.split(':', 1)
    command = parts[0].lower()
    amount = None
    if len(parts) == 2 and parts[1] != "":
        try:
            amount = float(parts[1])
        except ValueError:
            print(f"Invalid amount '{parts[1]}'. Must be a number.")
            sys.exit(1)
    return command, amount

def main():
    account = BankAccount(100)  # starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    command, amount = parse_arg(sys.argv[1])

    if command == "deposit":
        if amount is None:
            print("Usage for deposit: deposit:<amount>")
            sys.exit(1)
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:,.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw":
        if amount is None:
            print("Usage for withdraw: withdraw:<amount>")
            sys.exit(1)
        try:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount:,.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print(f"Invalid command '{command}'. Valid: deposit, withdraw, display.")

if __name__ == "__main__":
    main()
