import time

# Function to create topping decorators
def add_topping(topping, price):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"✅ {topping} added! (+₹{price}) 🍨")
            time.sleep(1)
            return func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator

# Ice cream sizes and base prices
sizes = {1: ("Small", 30), 2: ("Large", 60)}

# Available flavors
flavors = {1: "Vanilla", 2: "Butterscotch", 3: "Chocolate", 4: "Strawberry", 5: "Kulfi"}

# Toppings with prices
toppings = {1: ("✨ Sprinkles 🍩", 10), 2: ("🍫 Fudge 🍫", 20), 3: ("🥜 Nuts 🥜", 15), 4: ("🍯 Caramel 🍯", 25)}

selected_toppings = []

# Function to display menu options
def display_options(title, options):
    print(f"\n🎉 {title} 🎉\n" + "-" * 30)
    for key in options:
        value = options[key]
        if isinstance(value, tuple):  # Check if the value is a tuple
            print(f"{key}. {value[0]} - ₹{value[1]}")
        else:
            print(f"{key}. {value}")
    print("-" * 30)

# Function to get valid user input
def get_choice(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print("❌ Invalid choice! Please try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Welcome message
print("\n🎉 Welcome to the Ice Cream Shop! 🍦🎉")

# Get size choice
display_options("Choose Your Ice Cream Size", sizes)
size_choice = get_choice("📏 Enter your choice: ", sizes)
selected_size, total_price = sizes[size_choice]

# Get flavor choice
display_options("Choose Your Flavor", flavors)
flavor_choice = get_choice("🌈 Enter your choice: ", flavors)
selected_flavor = flavors[flavor_choice]

# Get topping choices
display_options("Available Toppings (Optional)", toppings)
while True:
    choice = input("✨ Enter topping number (0 to finish): ").strip()
    if choice == "0":
        break
    if choice.isdigit() and int(choice) in toppings:
        choice = int(choice)
        selected_toppings.insert(0, add_topping(*toppings[choice]))  # Maintain order of toppings
        total_price += toppings[choice][1]  # Add price
    else:
        print("❌ Invalid choice! Try again.")

# Apply toppings dynamically
def apply_toppings(func):
    for decorator in selected_toppings:
        func = decorator(func)
    return func

@apply_toppings
def get_icecream():
    print("\n🎊 Preparing your ice cream... 🍦✨")
    time.sleep(1)
    print(f"\n🍦 Your **{selected_size} {selected_flavor}** Ice Cream is Ready! 🍦")
    print("-" * 30, f"\n💰 Total Price: ₹{total_price}\n🍽️ Enjoy your treat! 🍽️\n")

# Serve the ice cream
get_icecream()
