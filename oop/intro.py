'''
object oriented programming
object - properties (attributes) and function (methods)
'''

class Character:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack}')

warrior = Character("Thor",100,50)
mage = Character("Gandalf",80,80)

warrior.attack_enemy()
mage.attack_enemy()
