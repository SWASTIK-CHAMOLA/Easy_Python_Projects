# validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

while True:
    a = input("Enter your name: ")
    a = a.replace(" ", "")
    if not a.isalpha():
        print("Username must only contain letters (no digits or spaces). Enter again.")
        continue
    if len(a) > 12:
        print("Username cannot be longer than 12 characters. Enter again.")
        continue
    break
print("Username accepted:", a)