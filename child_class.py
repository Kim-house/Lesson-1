class Bird:
    def __init__(self):
        print("Bird is ready")

    def whothis(abcd):
        print("Bird")

    def swim(fax):
        print("swim faster")

# creating child class
class Penguin(Bird):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print("Penguin is ready")

    def eat(seed):
        print(seed.name + " eat seeds")

peggy = Penguin("sue")
# peggy.swim()
# peggy.whothis()
peggy.eat()


