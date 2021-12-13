import random
import time
class Animal(object):
    """
    將貓和老鼠的共同特性抽象出來的類
    """
    def __init__(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)

    def move(self,move_skill):
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

    def is_vaild(self,value):
        if 1 <= value <= 10:
            return value
        elif value<1:
            return abs(value)
        elif value >10:
            return 10-(value-10)


class Cat(Animal):

    def __init__(self):
        super(Cat,self).__init__()
        self.power=100

    def move(self,move_skill= (-2,-1,0,1,2)):
        super(Cat,self).move(move_skill)
        self.power -= 1
    def eat(self):
        self.power += 20

class Mouse(Animal):

    def move(self,move_skill=(-1,0,1)):
        super(Mouse,self).move(move_skill)


def main():
    cat = Cat()
    mouses = [Mouse() for i in range(10)]
    while True:
        if cat.power <= 0:
            print('貓沒有體力了')
            break
        elif len(mouses) == 0:
            print('老鼠被吃光了!')
            break
        else:
            cat.move()
            for mouse in mouses:
                mouse.move()
                if cat.x == mouse.x and cat.y == mouse.y:
                    cat.eat()
                    mouses.remove(mouse)
                    print('老鼠被貓吃了!')
                    print('貓當前體力值為:%d' %(cat.power))
            else:
                print('貓沒有吃到老鼠，貓體力值:%d' %(cat.power))
        time.sleep(0.1)

if __name__ == '__main__':
    print('遊戲開始!'.center(50,'*'))
    main()
    