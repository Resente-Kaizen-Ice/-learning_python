"""class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("woof woof")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.add = address
        self.con = contact_number


owner1 = Owner("ice", "north wind subdv.", "09384003099")
dog1 = Dog("putaro", "shih tzu", owner1)
print(dog1.owner.name)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hi my name is {self.name} and I am {self.age} years old")


person1 = Person("Kaizen Ice", 24)
person1.greet()


from datetime import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def get_password(self):
        print(f"Email accessed at {datetime.now()}")
        return self._password

    def set_password(self, new_pass):
        if "@" in new_pass:
            self._password = new_pass


user1 = User("ice", " ABc_123   ")

print(user1.get_password())

user1.set_password("@avocado_lover123")

print(user1.get_password())

from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.em = email
        self.password = password

    def get_user(self):
        print(f"username is accessed at {datetime.now()}")
        return self.username

    def set_user(self, new_username):
        print(f"username is editted at {datetime.now()}")
        self.username = new_username

    def set_pass(self, new_pass):
        if "admin" in self.username:
            print(f"new password is set at {datetime.now()}")
            self.password = new_pass
        else:
            print("not authorize")

    def get_password(self):
        print(f"password accessed at {datetime.now()}")
        return self.password


user1 = User("kaizen123", "k@example.com", "12345")

print(f" initial user: {user1.get_user()}")

user1.set_user("maryjane123heart.admin")

print(f"edited user: {user1.get_user()}")

user1.set_pass("11111111")

print(f"editted password: {user1.get_password()} ")
"""

from datetime import datetime


class User:
    def __init__(self, email, password):
        self._email = email
        self._password = password

    @property
    def email(self):
        print(f"email is accessed at {datetime.now()}")
        return self._email

    @property
    def password(self):
        print(f"password is accessed at {datetime.now()}")
        return self._password

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            print(f"email edited at {datetime.now()}\nnew email is {new_email}")
            self._email = new_email
        else:
            print("not an email")

    @password.setter
    def password(self, new_pass):
        if "admin" in self.email:
            print(f"password edited at {datetime.now()}\nnew password is {new_pass}")
            self._password = new_pass
        else:
            print("unauthorize")


user1 = User("kaizen@email.com", "123")

print(f"email: {user1.email}\npassword: {user1.password}")

user1.email = "kaizen@iceresente@admin.com"

user1.password = "1111111"
