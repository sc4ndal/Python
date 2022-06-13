class car:
    # 멤버 변수
    # color=""
    # speed=0
    # model=""
    count=0

    #생성자 함수
    def __init__(self, color, speed, model):
        # print("자동차 생성됨")
        self.color = color
        self.speed = speed
        self.model = model


        car.count = car.count+1
    # 멤버 함수
    def upSpeed(self, value):
        self.speed+=value

    def dowonSpeed(self,value):
        self.speed-=value

    def stop(self):
        self.speed = 0

car1 = car("red", 0, "AAA")
# car1.color="red"
# car1.speed=0
# car1.model="AAA"

car2 = car("green", 0, "BBB")
# car2.color="green"
# car2.speed=0
# car2.model="BBB"

car3 = car("blue", 0, "CCC")
# car3.color="blue"
# car3.speed=0
# car3.model="CCC"

car1.upSpeed(30)
print("car1 | color %s | speed %dkm | model %s"%(car1.color,car1.speed,car1.model))

car2.upSpeed(60)
print("car2 | color %s | speed %dkm | model %s"%(car2.color,car2.speed,car2.model))

car3.upSpeed(90)
print("car3 | color %s | speed %dkm | model %s"%(car3.color,car3.speed,car3.model))

car1.stop()
print("car1 | speed %dkm"%car1.speed)

print("자동차 수 : %d"%car.count+"대")