balance  = 100000
while True:
    print("\nATM Menu.")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("enter your choice:")
    if choice == "1":
        print(f"Your balance is:${balance:.2f}")

    elif choice == "2":
        deposit = float(input("Enter the amount to deposit"))
        if deposit > 0:
            balance += deposit
            print(f"${deposit:.2} deposited successfully")

        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        withdraw = float(input("Enter the amount to withdraw:"))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f"${withdraw:.2f} withdrawn successfuly")

        else:
            print("Insufficient funds or invalid amount")

    elif choice == "4":
        print("Thank you for using ATM. Goodbye!")
    else:
        print("Invalid choice. Please try agin.")


