import Array as arr

class Character:

    def __init__(self,name, intHealth, intFeature,speed):
        self.abilities  = arr.array("Ram","Shield","Slice", "Climb")
        self.name = name
        self.health = intHealth
        self.ability = intFeature
        self.speed = speed

    def addHealth(self, bonusHealth):
        self.health+=bonusHealth
    def damage(self, tdamage):
        self.health -= tdamage

    def printStats(self):
        print("Name:" + self.name +"\n"+ "Health:" + str(self.health) + "\n" "Ability:" + self.ability + "\n" "Speed:" + str(self.speed))

    

#test
def main():
    char =  Character("Joe",5, "Ram", 5)
    char.addHealth(5)
    char.damage(2)
    char.printStats()
main()
