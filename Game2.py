#so I can randomly select enemies to fight
import random

#Variables for Player base stats
PlayerHealth = 100
PlayerAttack = 3

#Creates a class for the Enemies
class Enemy:

#Creates a function to store enemy stats    
    def __init__(self, name, health, attack, defence, loot):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.loot = loot
        
#Creates a function to print stats when called
    def Stats(self):
        return 'Stats: H-{} A-{} D-{} L-{}'.format(self.health, self.attack, self.defence, self.loot)
    
#Provides options for players turn
    def PlayerTurn(self):
        print ("Type to Attack, Run, get Stats, or Give Up: ")
        answer = input()

        if answer == "Attack":
            self.health = self.health - PlayerAttack
        elif answer == "Run":
            self.health = self.health - 1
        elif answer == "Stats":
            print(self.stats)
        else:
            print("you are defeated...")

#Calculates Enemies turn
    def EnemyTurn(self):
        print ("The enemy " + self.name + " " + "attacks...")
        PlayerHealth = PlayerHealth - (self.Attack)
        PlayerHealth = int(PlayerHealth)
        print ("Your health is now " + PlayerHealth)
        return int(PlayerHealth)

#Flavor Text 
    def BattleSystem(self):
        print ("An enemy {0.name} appears...".format(self))
    # Combat loop
    while PlayerHealth > 0 and self.Health > 0:
        PlayerAttack(self)
        print("The health of the {0.name} is now {0.health}.".format(self))
        if self.Health <= 0:
            break
        self.Attack(player)
        print("Your health is now {0.health}.".format(player))
    # Display outcome
    if PlayerHealth > 0:
        print("You killed the {0.name}.".format(enemy))
    elif self.health > 0:
        print("The {0.name} killed you.".format(enemy))
            
#Database of Enemy types and their stats
#Spider = Enemy("Spider",1,1,0,1)
#Skeleton = Enemy("Skeleton",2,2,1,2)
#Zombie = Enemy("Zombie",1,3,1,3)
#Goblin = Enemy("Goblin",3,3,3,5)
#Orc = Enemy("Orc",5,5,5,10)
#Troll = Enemy("Troll",10,10,10,100)
#Chest = Enemy("Chest",0,0,0,100)

enemies = [Enemy("Spider",1,1,0,1), Enemy("Skeleton",2,2,1,2),
               Enemy("Zombie",1,3,1,3), Enemy ("Goblin",3,3,3,5),
                   Enemy("Zombie",1,3,1,3), Enemy("Zombie",1,3,1,3), Enemy("Zombie",1,3,1,3),]

battle(Player(), random.choice(enemies))


