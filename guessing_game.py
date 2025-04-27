import random

ran = random.randint(1, 10)


def result(value):
    if value > ran:
        return "number is too high"
    if value < ran:
        return "number is too low"


while True:
    try:
        guess = int(input("guess the number: "))

        while not guess:
            print("please enter a number")
            guess = int(input("guess the number: "))

        attempts = 5

        while attempts > 0:
            if guess == ran:
                print(f"you got it! {guess} is indeed the answer")
                break
            else:
                print(result(guess))
                attempts -= 1
                print(f"you have {attempts}/s left")

                if attempts > 0:
                    guess = int(input("guess the number: "))
                else:
                    print(
                        "you have reached the maximum attempts, better luck next time!")

    except ValueError as e:
        print("please enter a number, ", e)

    restart = input("you want to play again?(yes/no)").lower()
    if restart == "no" or restart == "n":
        print("thank you for playing!")
        break
