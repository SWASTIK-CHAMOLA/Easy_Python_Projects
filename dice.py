import random
# ● ┌ ─ ┐ │ └ ┘

"┌───────────┐"
"│           │"
"│           │"
"│           │"
"└───────────┘"

dice_art = {
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘"),
    2:("┌───────────┐",
       "│  ●        │",
       "│           │",
       "│        ●  │",
       "└───────────┘"),
    3:("┌───────────┐",
       "│  ●        │",
       "│     ●     │",
       "│        ●  │",
       "└───────────┘"),
    4:("┌───────────┐",
       "│  ●     ●  │",
       "│           │",
       "│  ●     ●  │",
       "└───────────┘"),
    5:("┌───────────┐",
       "│  ●     ●  │",
       "│     ●     │",
       "│  ●     ●  │",
       "└───────────┘"),
    6:("┌───────────┐",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "└───────────┘")

}
dice = []
total = 0
no_of_dice = int(input("How many dice?: "))
for i in range(no_of_dice):
    dice.append(random.randint(1,6))
print(dice)
for i in range(no_of_dice):
    for j in dice_art.get(dice[i]):
        print(j)
for i in dice:
    total+=i
print(f"The total is: {total}")
