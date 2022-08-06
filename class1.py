
from os import name


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 인스턴스 생성시 자동으로 생성한다.
        self.home = "서울"
    def sound(self):
        print("이 강아지의 이름은 {0}이며 큰 소리를 내며 짖습니다. 사는곳은 {1}".format(self.name,self.home))

class DogMom(Dog):
    name = "꽁이"
    def sound2():
        print("이 강아지의 이름은 {0}이며 큰 소리를 내며 짖습니다.".format(name))

x = Dog("꽁이",12)
print(x.sound())

class Cat:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def hello(self):
        return print("반가워여 저는 {0}이에여 사는곳은 {1} 이에여".format(self.name,self.address))
    
a = Cat("김고양","강원무실동")
a.hello()