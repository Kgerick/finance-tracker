def show_menu():
    print("\n==== Finance Tracker ====")
    print("1) Add transaction")
    print("2) View all transactions")
    print("3) View Summary")
    print("4) Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            print("You chose: Add transaction")
        elif choice == "2":
            print("You chose: View all transactions")
        elif choice == "3":
            print("You chose: View Summary")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    main()
