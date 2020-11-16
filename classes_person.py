# creating a class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# adult1 = Person ("Lisa", 18)

# print(adult1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def turn (self):
         print(self.name + " you have turned", self.age)

sir = Person ("John", 20)
sir2 = Person ("Gerald", 50)
sir.turn()
sir2.turn()
# print(sir.age)

# def morning (names):
#     return("good morning ", names)

# def add (v, w):
#     z = v+w
#     return z


# print(add(3,4))
# morning("watunguyas")
# print(morning(24))

