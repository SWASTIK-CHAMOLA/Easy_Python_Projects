import random  # to randomize the slot places which display the output
import time    # to make delay in displaying the output

def slot_row():
    symbols = ['🍋', '🍒', '🍉', '⭐', '🍺']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("--------------")
    print(" | ".join(row))
    print("--------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Check for three matching symbols
        payouts = {'🍋': 2, '🍒': 3, '🍉': 4, '⭐': 5, '🍺': 10}
        return bet * payouts[row[0]]
    return 0  # No payout if symbols don’t match

def main():
    while True:
        initial_balance = input("Enter the amount of money you want to play with (Minimum ₹100): ")

        if not initial_balance.isdigit():
            print("❌ Invalid input! Please enter a valid number.")
            continue

        initial_balance = int(initial_balance)

        if initial_balance < 100:
            print("❌ Minimum balance required is ₹100. Please enter a higher amount.")
            continue
        else:
            break  # Exit loop once valid input is received

    balance = initial_balance  # Set user-defined balance

    while balance > 0:
        print(f"\nCurrent balance is ₹{balance}")

        bet = input("Enter your betting amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            print("Thank you for playing! Goodbye 👋")
            break

        if not bet.isdigit():
            print("❌ Invalid input! Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("❌ Bet must be greater than ₹0.")
            continue

        if bet > balance:
            print("❌ You have insufficient balance.")
            continue

        balance -= bet  # Deduct bet from balance

        print("\n🎰 Spinning the slot machine... 🎰\n")
        time.sleep(3) 

        row = slot_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You won ₹{payout}! 🎉")
            balance += payout  # Add payout to balance
        else:
            print("😞 No win this time. Try again! 😞")

    print(f"\nGame over! Your final balance is ₹{balance}")

if __name__ == '__main__':
    main()
