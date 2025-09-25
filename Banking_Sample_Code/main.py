def balance(c_balance):
    print(f"Your current balance is: ₹{c_balance:.2f}")

def withdraw(c_balance):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > c_balance:
        print("Insufficient funds!")
    elif amount <= 0:
        print("Invalid withdrawal amount!")
    else:
        c_balance -= amount
        print(f"Withdrawal successful! New balance: ₹{c_balance:.2f}")
    return c_balance

def deposit(c_balance):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        c_balance += amount
        print(f"Deposit successful! New balance: ₹{c_balance:.2f}")
    else:
        print("Invalid deposit amount!")
    return c_balance

def main():
    c_balance = 0.0  # Initialize balance
    this_function_runs = True

    while this_function_runs:
        print("\nWelcome to our banking program")
        print("1. To display balance")
        print("2. To withdraw money")
        print("3. To deposit money")
        print("4. To exit the program")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                balance(c_balance)
            elif choice == 2:
                c_balance = withdraw(c_balance)  # Update balance
            elif choice == 3:
                c_balance = deposit(c_balance)  # Update balance
            elif choice == 4:
                print("Thank you for using our program!")
                this_function_runs = False
            else:
                print("Invalid input! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
