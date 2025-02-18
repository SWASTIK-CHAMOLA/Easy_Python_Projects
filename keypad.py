# Simple 2-D Keypad Simulator made in python with tuples 

numpad = ((1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",0,"#"))
for row in numpad:
    for number in row:
        print(number,end=" ")
    print()
