class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성 되었습니다.')
        print(f'체력 {self.hp}, 공격력 {self.damage}')


marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)

wraith1 = Unit('레이스',80,5)

wraith2 = Unit('빼앗은 레이스',80,5)
wraith2.clocking = True  # 클래스 외부에서 변수를 확장할 수 있다. 단, 확장한 객체에만 적용.

if wraith2.clocking == True:
    print(f'{wraith2.name} 는 현재 클로킹 상태입니다.')