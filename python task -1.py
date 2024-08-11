import datetime

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal of {amount} on {datetime.datetime.now()}")
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit of {amount} on {datetime.datetime.now()}")
        print("Deposit successful. New balance:", self.balance)

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    pin = int(input("Enter your PIN: "))
    account = ATM(pin)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Check Transaction History")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.check_balance()
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 4:
            new_pin = int(input("Enter new PIN: "))
            account.change_pin(new_pin)
        elif choice == 5:
            account.check_transaction_history()
        elif choice == 6:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()