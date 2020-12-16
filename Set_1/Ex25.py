# Question 25
# Level 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later


class Person:

    name = "person"

    def __init__(self, name=None):
        self.name = name


eu = Person("Tiago")
print(Person.name, eu.name)

Tiago = Person()
Tiago.name = "Tiago"

print("{} name is {}", format(Person.name, Tiago.name))
