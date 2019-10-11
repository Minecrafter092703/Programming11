import random
import time
##dead = ""
##chosenBattlefield = ''

def chooseBattlefield():
    global battlefield
    battlefield = ''
    while battlefield != '1' and battlefield !='2':
        print('Which battlefield would you like to fight in? (1)Vimy Ridge or (2)Passchendaele')
        battlefield = input()

    return battlefield

def checkBattlefield():
    global dead
    dead = None
    print('You approach the Battlefield...')
    time.sleep(2)
    print('There are constant fire fights...')
    time.sleep(2)
    print('You hear a mortar flying above your head, you look up and...')
    print()
    time.sleep(2)

    friendlyBattlefield = str(random.randint(1, 2))
    print(friendlyBattlefield)

    if battlefield == friendlyBattlefield:
        print('It flies way past your head, you are safe!')
        dead = "no"
    else:
        print('The bomb comes crashing down, exploding and killing you and everyone around.')
        dead = "yes"
    return dead    

def chooseWeapon():
    global weapon
    weapon = ''
    while weapon != '1' and weapon !='2':
        print('You stumble upon a few pistols in the mud, which will you choose? (1)Mauser C96 or (2)Webley Bull Dog')
        weapon = input()

    return weapon

def checkWeapon():
    global dead
    dead = None
    print('You start walking towards the pistol...')
    time.sleep(2)
    print('You bend down to pick the weapon up and...')
    print()
    time.sleep(2)

    friendlyWeapon = str(random.randint(1, 2))
    print(friendlyWeapon)

    if weapon == friendlyWeapon:
        print("A bullet flies right by your head but you're safe!")
        dead = "no"
    else:
        print("A german sniper shoots you dead in the eyes.")
        dead = "yes"
    return dead

def displayIntro():
    print('''You are in the year 1917 and you have been enrolled into
the British army, you come apon two identical trenches on the battlefield,
one of them is an ally trench, the other trench is full of enemies
ready to put bullets through your helmet.''')
    print()
    
def chooseTrench():
    trench = ''
    while trench != '1' and trench !='2':
        print('Which trench do you dare enter? (1 or 2)')
        trench = input()

    return trench

def checkTrench(chosenTrench):
    print('You approach the mud filled trench...')
    time.sleep(2)
    print("It's dark, filled with empty bullet shells and rat infested...")
    time.sleep(2)
    print('A large group of soldiers jump out in front of you! They take aim and...')
    print()
    time.sleep(2)

    friendlyTrench = random.randint(1, 2)

    if chosenTrench == str(friendlyTrench):
        print('Gives you food and everything you lost!')
    else:
        print("They all fire their Gewehr 98's and that is your last breath you'll ever take.")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    battlefieldNumber = chooseBattlefield()
    checkBattlefield()
    if dead == "no":
        chooseWeapon()
        checkWeapon()
        displayIntro()
        trenchNumber = chooseTrench()
        checkTrench(trenchNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
