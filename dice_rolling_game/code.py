import random

while True:
    x=random.randint(1,6)
    y=random.randint(1,6)
    ans=input(print("Roll the dice?(y/n):"))
    if (ans=="y"):
        print(f"({x},{y})")
    else:
        break
