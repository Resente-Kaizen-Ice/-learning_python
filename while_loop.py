
user = input("dont enter a number or null value: ")

while not user or user.isdigit():
    print("i told you to dont enter a number or null value, are you stupid?\n try again")

    user = input("dont enter a number or null value: ")

print("value is " + user)
