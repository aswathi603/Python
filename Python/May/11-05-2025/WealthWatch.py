import sys

class Transaction:
    def __init__(self, amount, t_type, category):
        self.amount = amount
        self.type = t_type.lower()
        self.category = category

    def __str__(self):
        return f"{self.type.capitalize()} of {self.amount} in category '{self.category}'"

class ExpenseIncomeTracker:
    def __init__(self, currency_symbol='$'):
        self.transactions = []
        self.total_saving = 0.0
        self.currency_symbol = currency_symbol

    def add_transaction(self, amount, t_type, category):
        if t_type.lower() not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'")
        transaction = Transaction(amount, t_type, category)
        self.transactions.append(transaction)
        if transaction.type == 'income':
            self.total_saving += transaction.amount
        else:
            self.total_saving -= transaction.amount
        print(f"Transaction Added: {transaction}")
        print(f"Total saving: {self.currency_symbol}{self.total_saving:.2f}")

    def list_transactions(self):
        if not self.transactions:
            print("No transactions added yet.")
            return
        print("All Transactions:")
        for idx, t in enumerate(self.transactions, start=1):
            print(f"{idx}. {t}")
        print(f"Current total saving: {self.currency_symbol}{self.total_saving:.2f}")

def main():
    print("Welcome to Expense and Income Tracker CLI Wealth Watch App!")
    currency_symbol = input("Choose currency symbol (default $): ").strip()
    if not currency_symbol:
        currency_symbol = '$'
    tracker = ExpenseIncomeTracker(currency_symbol)

    print("Commands:")
    print("  ADD transition - to add a transaction")
    print("  LIST - to list all transactions")
    print("  EXIT - to quit the app")

    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() == 'exit':
                print("Exiting. Goodbye!")
                break
            elif user_input.lower() == 'list':
                tracker.list_transactions()
            elif user_input.lower() == 'add transition':
                # Prompt for details
                while True:
                    amount_input = input("Amount: ").strip()
                    try:
                        amount = float(amount_input)
                        if amount <= 0:
                            print("Amount must be positive. Please enter again.")
                            continue
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                while True:
                    t_type = input("Type (income/expense): ").strip().lower()
                    if t_type not in ['income', 'expense']:
                        print("Invalid type. Please enter 'income' or 'expense'.")
                    else:
                        break
                category = input("Category: ").strip()
                tracker.add_transaction(amount, t_type, category)
            else:
                print("Unknown command. Available commands: ADD transition, LIST, EXIT")
        except KeyboardInterrupt:
            print("\nExiting. Goodbye!")
            break
        except Exception as ex:
            print(f"Error: {ex}")

if __name__ == "__main__":
    main()


