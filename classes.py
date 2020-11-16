class Parrot:
    """
    We are creating a python class
    """

    # class attribute 
    species ="Bird"

    #instance attribute 

    def __init__(self,name, age):
        self.name = name
        self.age = age
 
#<------------------------------------------------->
#creating an object

liz = Parrot("gerald", 10)
ben = Parrot("kamau", 20)

#<--------------------------------------------------->

# accessing the class attributes 
print("Liz is a {}".format(liz.__class__.species))
print ("ben is a {}". format(ben.__class__.species))

# <----------------------------------------------------->
# accessing the instance attributes 
print(liz.name, liz.age)

