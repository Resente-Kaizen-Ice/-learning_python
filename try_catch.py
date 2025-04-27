
try:
    name = input("what is your name: ")
    null = "".strip()  # strip is just to remove any white space or yung space mo tanga ka kase

    while name == null:
        print("name cannot be null, please enter a name")

        name = input("what is your name: ")
    try:
        # convert ko name into int kase gusto ko malaman ni program if number ba yung name or hinde
        int(name)
        raise ValueError("value cannot be a number")
    except ValueError as ve:
        if str(ve) == "value cannot be a number":
            print(ve)
        else:
            print("hello " + name)

except Exception as e:
    print("something went wrong", e)
