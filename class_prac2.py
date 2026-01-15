# 일반 유닛
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛(상속)
class AttackUnit(Unit): #자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self,location):
        print(f'{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')


    def damaged(self,damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp}입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴 되었습니다.')


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,location):
        print(f'{self.name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]')


class FlyableAttackUnit(AttackUnit,Flyable):   # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly("5시")


