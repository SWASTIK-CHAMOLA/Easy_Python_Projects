# Basic and or not example use with string input
while True:
    print("enter True and False for understanding logical operators 'and', 'or', 'not'\n")
    b= input("enter True or False: ")
    c = input("enter True or False: ")
    b.lower()
    c.lower()
    if b == 'true' or b == 'false':
        if c == 'true' or c == 'false':
            print("and operator output", b and c)
            print("or operator output", b or c)
            print("not c operator output", not c)
            print("not b operator output", not b)
        else:
            print("invalid input")
    else:
        print("invalid input")
    a = int(input("enter 0 to exit or 1 to continue: "))
    if a == 0:
        break
    else:
        continue




