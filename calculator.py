print("Welcome to t=he calculator")
print("\n")
print("Press 1 for + 2 for - 3 for * and 4 for /")
a = int(input("enter the choice: "))
if a not in [1, 2, 3,4]:
    print("Invalid choice")
elif a == 1:
    b = int(input("enter the 1st number: "))
    c = int(input("enter the 2nd number: "))
    print(f"{b} + {c} = {b+c}")
elif a == 2:
    b = int(input("enter the 1st number: "))
    c = int(input("enter the 2nd number: "))
    print(f"{b} - {c} = {b-c}")
elif a == 3:
    b = int(input("enter the 1st number: "))
    c = int(input("enter the 2nd number: "))
    print(f"{b} * {c} = {b*c}")
elif a == 4:
    b = int(input("enter the 1st number: "))
    c = int(input("enter the 2nd number: "))
    print(f"{b} / {c} = {b/c}")
