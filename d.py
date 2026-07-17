class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

tom = Robot("Tom", 1.5)
jerry = Robot("Jerry", 2.0)

print("Hi i am a robot named: {} and i am version: {} ".format(tom.name, tom.version))
print("Hi i am a robot named: {} and i am version: {} ".format(jerry.name, jerry.version))