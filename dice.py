import random

start = input("play(Y/N): ")

while start.lower() == "y":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    dice = "the number is [" + str(dice1) + ", " + str(dice2) + "]"

    print(dice)
    start = input("play(Y/N): ")
    continue

print("thank you for playing")
