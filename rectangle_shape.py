#Make a rectangle from user input
a = int(input("enter no of rows of your rectangle: "))
b = int(input("enter no of columns of your rectangle: "))
symbol = input("enter the symbol you want to use: ")
for i in range(0,a):
    for j in range(0,b):
        print(symbol,end = "")
    print()
