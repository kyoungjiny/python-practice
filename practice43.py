class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flayble 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship=FlyableUnit()
   