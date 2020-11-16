# class Computer:
#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price 

# c = Computer()
# c.sell()

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()


class Person:
    def __init__(self):
        self.__name = "john"
        self.__age = 20

    def write(self):
        print("my name is {}, my age is {}".format(self.__name, self.__age))

    def new_name(self, name, age):
        self.__name = name
        self.__age = age

p = Person()
p.write()
# print(p.__name)
p.__name="ken"
p.__age=18
p.write()

p.new_name("jamo", 31)
p.write()