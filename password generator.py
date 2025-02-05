# Password Generator in Python
import random

a = ['A', 'a','B', 'b','C', 'c','D', 'd','E', 'e','F', 'f','G', 'g','H', 'h','I', 'i','J', 'j','K', 'k','L', 'l','M', 'm','N', 'n','O', 'o','P','p','Q', 'q','R', 'r','S', 's','T', 't','U', 'u','V', 'v','W', 'w','X', 'x','Y', 'y','Z','z']
b = ['1','2','3','4','5','6','7','8','9','0']
c = ['!','@','#','$','%','^','&','*','(',')','+']
print("welcome to password generator!")
k = int(input("How many letters do you want in your password\n"))
l = int(input("How many nos do you want in your password\n"))
m = int(input("How many symbols do you want in your password\n"))
password = ""
for i in range(1,k+1):
    char = random.choice(a)
    password = password+char
for i in range(1,l+1):
    char = random.choice(b)
    password = password+char
for i in range(1,m+1):
    char = random.choice(c)
    password = password+char
print(password)
