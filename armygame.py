# IMPORT
import os
import time
from random import *

# TITLE
os.system('clear')
print("|--------------------------------|")
print("|--------BARN'S ARMY GAME--------|")
print("|--------------------------------|")

# DEFINE BATTLE RULES
def custom_battle():

    # INTRODUCTION
    os.system('clear')
    input("Please start by telling us about Army 1.\nPress Enter to continue...")

    ## ARMY 1 STAT SETUP ##
    # soldiers
    army1_soldier = input('Which character to represent Army 1?\n')
    army1_size = int(input('How many soldiers in Army 1?\n'))
    while (army1_size > 5000):
        army1_size = int(input('Please choose a smaller number:\n'))
    # hp and dmg
    army1_hp = int(input('What health value should Army 1 units have?\n'))
    while (army1_hp > 5000):
        army1_hp = int(input('Please choose a smaller number:\n'))
    army1_dmg = int(input('How much damage do Army 1 units have?\n'))
    while (army1_dmg > 5000):
        army1_dmg = int(input('Please choose a smaller number:\n'))
    army1_chance = int(input("What is Army 1's Chance to Crit (out of 100)?\n"))
    while (army1_chance > 100):
        army1_chance = int(input('Please be reasonable.\n'))
    # name
    army1 = input('What name/race to give to Army 1?\n')

    # TRANSITION
    input("Wow, seems strong! Now please, tell us about Army 2.\nPress Enter to continue...")

    ## ARMY 2 STAT SETUP ##
    # soldiers
    army2_soldier = input('Which character to represent Army 2?\n')
    army2_size = int(input('How many soldiers in Army 2?\n'))
    while (army2_size > 5000):
        army2_size = int(input('Please choose a smaller number:\n'))
    # hp and dmg
    army2_hp = int(input('What health value should Army 2 units have?\n'))
    while (army2_hp > 5000):
        army2_hp = int(input('Please choose a smaller number:\n'))
    army2_dmg = int(input('How much damage do Army 2 units have?\n'))
    while (army2_dmg > 5000):
        army2_dmg = int(input('Please choose a smaller number:\n'))
    army2_chance = int(input("What is Army 2's Chance to Crit (out of 100)?\n"))
    while (army2_chance > 100):
        army2_chance = int(input('Please be reasonable.\n'))
    # name
    army2 = input('And finally, what name/race to give to Army 2?\n')

    # ASSIGN NEW SOLDIER HP
    soldier1_currhp = army1_hp
    soldier2_currhp = army2_hp
    army1_crit = False
    army2_crit = False
    attack_count = 0

    # pause for user input
    input('Press Enter to begin the battle...')

    # ACTUAL BATTLE LOGIC
    while (army1_size > 0) and (army2_size > 0):
        # PRINT BATTLEFIELD
        os.system('clear')
        print('Attack Phase: ' + str(attack_count) + '\n\n')
        print(army1 + ':')
        print(army1_soldier*army1_size + '\n')
        print('vs.\n')
        print(army2 + ':')
        print(army2_soldier*army2_size + '\n')
        time.sleep(0.08)

        # CHECK FOR CRIT SUCCESS/FAIL
        # check army 1 crit
        army1_roll = randint(0,101)
        if (0 < army1_roll <= army1_chance):
            army1_crit = True
        else:
            army1_crit = False
        # check army 2 crit
        army2_roll = randint(0,101)
        if (0 < army2_roll <= army2_chance):
            army2_crit = True
        else:
            army2_crit = False

        # DEAL DAMAGE, NEW HP
        # apply army 1 dmg
        if army1_crit:
            print(army1 + ': CRIT SUCCESS')
            time.sleep(0.15)
            soldier2_currhp = soldier2_currhp - 2*army1_dmg
        else:
            soldier2_currhp = soldier2_currhp - army1_dmg
        # apply army 2 dmg
        if army2_crit:
            print(army2 + ': CRIT SUCCESS')
            time.sleep(0.15)
            soldier1_currhp = soldier1_currhp - 2*army2_dmg
        else:
            soldier1_currhp = soldier1_currhp - army2_dmg

        # reduce army size if dead
        if (soldier1_currhp <= 0):
            army1_size = army1_size-1
            soldier1_currhp = army1_hp
            attack_count = attack_count+1
        if (soldier2_currhp <= 0):
            army2_size = army2_size-1
            soldier2_currhp = army2_hp
            attack_count = attack_count+1

        # CHECK FOR WIN CONDITIONS
        if (army1_size <= 0) and (army2_size <= 0):
            print('------------------------------------------------------------')
            print('This war is a DRAW!')
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break
        elif (army1_size <= 0) and (army2_size > 0):
            print('------------------------------------------------------------')
            print('VICTORY to ' + army2 + '!')
            print(army2_soldier*army2_size)
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break
        elif (army1_size > 0) and (army2_size <= 0):
            print('------------------------------------------------------------')
            print('VICTORY to ' + army1 + '!')
            print(army1_soldier*army1_size)
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break

def rec_battle():
    # SET DEFAULTS INSTEAD OF USER
    os.system('clear')

    army1 = 'BARNS'
    army1_soldier = '[B]'
    army1_size = 175
    army1_hp = 100
    army1_dmg = 75
    army1_chance = randint(0,101)

    army2 = 'NARBS'
    army2_soldier = '[N]'
    army2_size = 50
    army2_hp = 300
    army2_dmg = 50
    army2_chance = randint(0,101)

    print('-------------------------------')
    print('--------BARNS-vs.-NARBS--------')
    print('-------------------------------')
    print('SOLDIER: [B]       [N] ')
    print('SIZE:    175       50  ')
    print('HP:      100       300 ')
    print('DMG:     75        50  ')
    print('CHANCE:  ' + str(army1_chance) + '        ' + str(army2_chance) + '  ')
    print('-------------------------------')

    # ASSIGN NEW SOLDIER HP
    soldier1_currhp = army1_hp
    soldier2_currhp = army2_hp
    army1_crit = False
    army2_crit = False
    attack_count = 0

    input('Press Enter to begin the battle...')

    while (army1_size > 0) and (army2_size > 0):
        # PRINT BATTLEFIELD
        os.system('clear')
        print('Attack Phase: ' + str(attack_count) + '\n\n')
        print(army1 + ':')
        print(army1_soldier*army1_size + '\n')
        print('vs.\n')
        print(army2 + ':')
        print(army2_soldier*army2_size + '\n')
        time.sleep(0.08)

        # CHECK FOR CRIT SUCCESS/FAIL
        # check army 1 crit
        army1_roll = randint(0,101)
        if (0 < army1_roll <= army1_chance):
            army1_crit = True
        else:
            army1_crit = False
        # check army 2 crit
        army2_roll = randint(0,101)
        if (0 < army2_roll <= army2_chance):
            army2_crit = True
        else:
            army2_crit = False

        # DEAL DAMAGE, NEW HP
        # apply army 1 dmg
        if army1_crit:
            print(army1 + ': CRIT SUCCESS')
            time.sleep(0.15)
            soldier2_currhp = soldier2_currhp - 2*army1_dmg
        else:
            soldier2_currhp = soldier2_currhp - army1_dmg
        # apply army 2 dmg
        if army2_crit:
            print(army2 + ': CRIT SUCCESS')
            time.sleep(0.15)
            soldier1_currhp = soldier1_currhp - 2*army2_dmg
        else:
            soldier1_currhp = soldier1_currhp - army2_dmg

        # reduce army size if dead
        if (soldier1_currhp <= 0):
            army1_size = army1_size-1
            soldier1_currhp = army1_hp
            attack_count = attack_count+1
        if (soldier2_currhp <= 0):
            army2_size = army2_size-1
            soldier2_currhp = army2_hp
            attack_count = attack_count+1

        # CHECK FOR WIN CONDITIONS
        if (army1_size <= 0) and (army2_size <= 0):
            print('------------------------------------------------------------')
            print('This war is a DRAW!')
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break
        elif (army1_size <= 0) and (army2_size > 0):
            print('------------------------------------------------------------')
            print('VICTORY to ' + army2 + '!')
            print(army2_soldier*army2_size)
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break
        elif (army1_size > 0) and (army2_size <= 0):
            print('------------------------------------------------------------')
            print('VICTORY to ' + army1 + '!')
            print(army1_soldier*army1_size)
            print('The battle raged on for ' + str(attack_count+1) + ' turns...')
            break

# BATTLE START
battletype = input('Would you like to use the recommended settings? [Y/n] \n')

while (battletype!='Y') and (battletype!='n'):
    os.system('clear')
    print('Please enter a valid response:')
    battletype = input('Would you like to use the recommended settings? [Y/n] \n')

if (battletype=='Y'):
    rec_battle()
else:
    custom_battle()
