import random

def rpscore(p1, p2):
    if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return 1
    elif p1 == p2:
        return 0
    else:
        return -1

y = input("Alright, tell me your choice: Rock, Paper or Scissors? ")
options = ["rock", "paper", "sissors"]
y= y.lower()
x = random.choice(options)
result = rpscore(y,x)
if result == 1:
    print("NO WAY! YOU WIN! Ugh, again! Again! ｡゜(｀Д´)゜｡")
elif result == 0:
    print("We picked the same thing. Talk about copycat.")
else:
    print("Hah! I won! Better luck next time, loser. :P")
