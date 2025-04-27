contacts = {
    "bob": ["012345", "bob@example.com"],
    "kate": ["555555", "kate@example.com"]
}

# print(contacts["bob"][1])

for contact, info in contacts.items():  # .items() para makuha yung lahat ng laman ni dictionary(key ex.bob and kate,,, and value ex. 012345 and 55555)
    print(f"{contact} - Phone - {info[0]}, Email - {info[1]}")

contacts["bob"][0] = "2222222"

print(f"bob: {contacts["bob"]}")
