import yfinance as yf

class Investment:
    def __init__(self, symbol, shares, buy_price):
        self.symbol = symbol
        self.shares = shares
        self.buy_price = buy_price

    def current_value(self):
        stock_data = yf.Ticker(self.symbol)
        current_price = stock_data.history(period='1d')['Close'].iloc[-1]
        return current_price * self.shares

class User:
    def __init__(self, username):
        self.username = username
        self.investments = []

    def add_investment(self, symbol, shares, buy_price):
        investment = Investment(symbol, shares, buy_price)
        self.investments.append(investment)

    def remove_investment(self, symbol):
        self.investments = [inv for inv in self.investments if inv.symbol != symbol]

    def view_investments(self):
        return [(inv.symbol, inv.shares, inv.buy_price, inv.current_value()) for inv in self.investments]

users = {}

def main_menu():
    print("\n Main Menu ")
    print("1. Add User")
    print("2. Add Investment")
    print("3. Remove Investment")
    print("4. View Investments")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            if username in users:
                print("User  already exists.")
            else:
                users[username] = User(username)
                print(f"User  '{username}' added.")
            break
        elif choice == '2':
            username = input("Enter username: ")
            if username not in users:
                print("User  does not exist.")
                continue
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            buy_price = float(input("Enter buy price: "))
            users[username].add_investment(symbol, shares, buy_price)
            print("Investment added.")
            break

        elif choice == '3':
            username = input("Enter username: ")
            if username not in users:
                print("User  does not exist.")
                continue
            symbol = input("Enter stock symbol to remove: ")
            users[username].remove_investment(symbol)
            print("Investment removed.")
            break
        elif choice == '4':
            username = input("Enter username: ")
            if username not in users:
                print("User  does not exist.")
                continue
            investments = users[username].view_investments()
            if investments:
                print("\nCurrent Investments:")
                for symbol, shares, buy_price, current_value in investments:
                    print(f"Symbol: {symbol}, Shares: {shares}, Buy Price: ${buy_price}, Current Value: ${current_value:.2f}")
            else:
                print("No investments found.")
            break

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()