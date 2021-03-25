import random

weapons = ['sword', 'bow', 'arrows', 'dagger', 'potions', 'staff']
inventory = []
monster_heads = ['ent head', 'bigfoots head', 'centaur head', 'troll head', 'giant crabs head']
possible_items = ['potion of health', 'relic 1', 'relic 2', 'relic 3']
health = 100
monsters_health = 0
dammage = 0

def battle(dammage, health, monsters_health):
    monsters = ['Ent', 'Bigfoot', 'Centaur', 'Troll', 'Giant Crab']
    enemy = random.randint(0,4)
    if enemy == 0:
        print("An ent attacks you")
    elif enemy == 1:
        print("Bigfoot attacks")
    elif enemy == 2:
        print ("A lone centaur sees you as easy prey fend him off")
    elif enemy == 3:
        print ("A large ugly troll swings a larger club at you defend yourself")
    else:
        print ("A giant crab moves towards you")

    monsters_health = random.randint(50,200)
    if monsters_health < 75:
        print("This is a weak monster")
    elif monsters_health > 76 and monsters_health < 150:
        print("This is a strong monster")
    elif monsters_health > 151:
        print("This is a mighty monster keep your wits about you")

    while monsters_health > -1:
        if warrior == "swordsman":
            print("do you want to:\n 1.Slash\n 2.Chop\n 3.Stab")

            try:
                attack = int(input("which one do you want to pick (1/2/3)"))
                if attack == 1:
                    dammage = random.randint(20,30)
                if attack == 2:
                    dammage = random.randint(20,35)
                if attack == 3:
                    dammage = random.randint(20,40)
            except:
                print("please type in a number")

                
        elif warrior == "archer":
            print ("do you want to:\n 1.Shoot arrow\n 2.Shoot fire arrow\n 3.Stab")

            try:
                attack = int(input("which one do you want to pick (1/2/3)"))
                if attack == 1:
                    dammage = random.randint(20,30)
                if attack == 2:
                    dammage = random.randint(30,45)
                if attack == 3:
                    dammage = random.randint(20,25)
            except:
                print("please type in a number")
                
                
        elif warrior == "mage":
            print ("do you want to:\n 1.Shoot fireball\n 2.Cast lightning bolt\n 3.Throw a damaging potion")

            try:
                attack = int(input("which one do you want to pick (1/2/3)"))
                if attack == 1:
                    dammage = random.randint(20,35)
                if attack == 2:
                    dammage = random.randint(20,40)
                if attack == 3:
                    dammage = random.randint(20,30)
            except:
                print("please type in a number")
                
        
        monsters_health = monsters_health - dammage

        miss = random.randint(0,2)
        if miss == 0:
            health = health - random.randint(15,25)
            print("the monster hits you")
        else:
            print("The monster misses his attack")

    if monsters_health < -1:
        print ("You have defeted this monster")
        if enemy == 0:
            inventory.append('ent head')
        elif enemy == 1:
            inventory.append('bigfoots head')
        elif enemy == 2:
            inventory.append('centaurs head')
        elif enemy == 3:
            inventory.append('trolls head')
        else:
            inventory.append('giant crabs head')
        print("In your inventory you now have " + str(inventory))  

    if health < -1:
        print("a monster has slain you, try regaining health by sleeping next time")
        quit()
    
failure = True
while failure == True:
    warrior = input("please pick your warrior either a swordsman, an archer or a mage you must type it all in lower case")
    if warrior == "swordsman":
        inventory.append('sword')
        failure = False
        print ("Your inventory contains" + str(inventory))

    if warrior == "archer":
        inventory.append('arrows')
        inventory.append('bow')
        inventory.append('dagger')
        failure = False
        print ("Your inventory contains" + str(inventory))

    if warrior == "mage":
        inventory.append('potions')
        inventory.append('staff')
        failure = False
        print ("Your inventory contains" + str(inventory))

    if failure == True:
        print("You didn't type in a valid class or you didn't type the whole class in lower case please try again")

battle(dammage, health, monsters_health)

if inventory == ['relic 1']:
    possible_items.remove('relic 1')
    print ("2 more to find")

if inventory == ['relic 2']:
    possible_items.remove('relic 2')
    print ("1 more left keep going")

if inventory == ['relic 1', 'relic 2', 'relic 3']:
    possible_items.remove('relic 3')
    print ("you have won the game")
    quit()
