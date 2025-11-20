from transactions import add_transaction, list_transactions, show_summary
from storage import load_transactions, save_transactions

def show_menu():
    print("\n==== Finance Tracker ====")
    print("1) Add transaction")
    print("2) View all transactions")
    print("3) View Summary")
    print("4) Exit")

def main():
    load_transactions()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            save_transactions()
            print("Saved. Goodbye.")
            break
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    main()
