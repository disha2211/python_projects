import random

count=0
while True:
    x=random.randint(1,6)
    y=random.randint(1,6)
    ans=input(print("Roll the dice?(y/n):")).lower()
    if (ans=="y"):
        print(f"({x},{y})")
        count +=1 
        print(f"Number of times dice rolled = {count}")
    elif (ans=="n"):
        print("Game Over")
        break
    else:
        print("Invalid choice")
