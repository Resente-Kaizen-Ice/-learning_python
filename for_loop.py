'''num = int(input("insert a number: "))

for i in range(0, num):  # i is variable name, range is the range of loop, 0 is the beginning index, num is the ending index (where to stop the loop)
    print(i + 1)'''

column = int(input("number of columns: "))
row = int(input("number of rows: "))
symbol = input("what symbol to use: ")

for i in range(row):
    for j in range(column):
        # end="" ay para nde mag nextline kumbag dikit dikit, so column = 3, @@@ instead of @\n @\n @\n
        print(symbol, end="")
    print()
