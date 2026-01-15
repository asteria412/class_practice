# 일반 유닛
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):            # 2개 이상을 상속받을 때 super()를 쓰면 마지막 클래스의 init함수 호출
        super().__init__()         # 각각 호출하려면 명시하여야 함.