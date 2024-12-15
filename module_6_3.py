import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz > 0:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you O_O")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)
    def dive_in(self, dz):
        self._cords[2] = int(self._cords[2] - abs(dz) * (self.speed / 2))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    
    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        self.sound = 'Click-click-click'
        super().__init__(speed)


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()