try:
    employee = {}

    number = int(input("number of employee: "))

    def compute(sal, no, ha):
        return (sal * no) - (sal/2 * ha)

    for i in range(number):
        user = input("enter name: ")
        salary = float(input("enter salary: "))
        days = int(input("number of days of work: "))
        half = input("any half day: ").lower()

        if half == "yes" or half == "y":
            numberOfHalf = int(input("how many half days: "))
        else:
            numberOfHalf = 0

        total = compute(salary, days, numberOfHalf)

        employee[user] = total

    for person in employee.items():
        print(person)

except Exception as e:
    print("an error has occured", e)
