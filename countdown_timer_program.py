import time
user_time=int(input("enter your time in seconds: "))
for i in range(user_time,0,-1):
    seconds = i % 60
    minutes = i // 60
    hours = i // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #used format specifier to display 2 digits padding
    time.sleep(1)

print("Wake Up!")