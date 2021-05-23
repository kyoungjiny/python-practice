class Unit:
    def __init__(self, name,hp):
        self.name=name
        self.hp=hp

class AttackUnit(Unit):
    def __init__(self, name,hp,damage):
        Unit.__init__(self,name,hp)
        self.damage=damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,self.damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location,self.flying_speed))

class FlyableAttckUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self,flying_speed)

valkyrie=FlyableAttckUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
     
