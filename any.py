import random
import math

class Warrior:
    def __init__(self, name='Warrior', health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax
    
    def attack(self):
        attackAmt = self.attackMax * (random.random() + .5)
        return attackAmt
    
    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt


class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            
            if self.getAttackResult(warrior1, warrior2) == "K.O":
                print('K.O')
                break

            if self.getAttackResult(warrior2, warrior1) == "K.O":
                print('K.O')
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAattackAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAattackAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        print('{} attacks {} and deals {} damage'.format(warriorA.name, warriorB.name, damage2WarriorB))
        print('{} is down to {} health'.format(warriorB.name,warriorB.health))
        if warriorB.health <= 0:
            print('{} is the winner'.format(warriorA.name))
            return 'K.O'
        else:
            return 'Fight Again'

def main():
    sanic = Warrior('Sanic', 50, 20, 10)
    link = Warrior('Link', 50, 20, 10)
    battle = Battle()
    battle.startFight(sanic, link)

main()