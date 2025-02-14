# Python compound interest calculator 

def is_valid(value):    # Check if the input is a valid number
    try:
        float(value)
        return True
    except ValueError:
        return False
principal = 0
rate = 0
time = 0
while principal <= 0:
    principal1 = input("Enter principal: ")
    if is_valid(principal1):
        principal = float(principal1)
        if principal <= 0:
            print("Please enter a valid positive number.")
    else:
        print("Invalid input! Please enter a numeric value for principal.")
while rate <= 0:
    rate1 = input("Enter Rate: ")
    if is_valid(rate1):
        rate = float(rate1)
        if rate <= 0:
            print("Please enter a valid positive number.")
    else:
        print("Invalid input! Please enter a numeric value for rate.")
while time <= 0:
    time1 = input("Enter Time: ")
    if is_valid(time1):
        time = float(time1)
        if time <= 0:
            print("Please enter a valid positive number.")
    else:
        print("Invalid input! Please enter a numeric value for time.")
print(f"Principal is {principal}")
print(f"Rate is {rate}")
print(f"Time is {time}")
total = principal * pow((1 + rate / 100), time)
print(f"Amount after {time} year/s is: {total:,.3f}")
