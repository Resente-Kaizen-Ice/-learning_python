fruits = ["apple", "banana", "mango"]

# print(fruits[2])

for fruit in fruits:
    print(fruit)

fruits.insert(1, "kiwi")
fruits.append("avocado")

for fruit in fruits:
    print("insert " + fruit)

fruits.pop(2)

for fruit in fruits:
    print("pop " + fruit)

fruits.clear()

print("fruit is gone")
