# IMPORT
import os
import time

# TITLE
os.system('clear')
print("|----------------|")
print("|BARN'S ARMY GAME|")
print("|----------------|")

# DEFINE BATTLE RULES
def battle():
    # INTRODUCTION
    input("Thanks for playing Barn's Army Game! Press Enter to continue...")
    input("Please start by telling us about Army 1. Press Enter to continue...")
    ## ARMY 1 STAT SETUP ##
    # soldiers
    army1_soldier = input('Which character to represent Army 1?\n')
    army1_size = int(input('Size of Army 1?\n'))
    while (army1_size > 5000):
        army1_size = int(input('Please choose a smaller number:\n'))
    # hp and dmg
    army1_hp = int(input('What health value should Army 1 units have?\n'))
    while (army1_hp > 5000):
        army1_hp = int(input('Please choose a smaller number:\n'))
    army1_dmg = int(input('How much damage do Army 1 units have?\n'))
    while (army1_dmg > 5000):
        army1_dmg = int(input('Please choose a smaller number:\n'))

    # TRANSITION
    input("Wow, seems strong! Now please, tell us about Army 2. Press Enter to continue...")
    ## ARMY 2 STAT SETUP ##
    # soldiers
    army2_soldier = input('Which character to represent Army 2?\n')
    army2_size = int(input('Size of Army 2?\n'))
    while (army2_size > 5000):
        army2_size = int(input('Please choose a smaller number:\n'))
    # hp and dmg
    army2_hp = int(input('What health value should Army 2 units have?\n'))
    while (army2_hp > 5000):
        army2_hp = int(input('Please choose a smaller number:\n'))
    army2_dmg = int(input('How much damage do Army 2 units have?\n'))
    while (army2_dmg > 5000):
        army2_dmg = int(input('Please choose a smaller number:\n'))

    # ASSIGN NEW SOLDIER HP
    soldier1_currhp = army1_hp
    soldier2_currhp = army2_hp

    # ACTUAL BATTLE LOGIC
    while (army1_size > 0) and (army2_size > 0):
        # PRINT BATTLEFIELD
        os.system('clear')
        print(army1_soldier*army1_size + '\n')
        print('vs.\n')
        print(army2_soldier*army2_size + '\n')
        time.sleep(0.1)

        # DEAL DAMAGE, NEW HP
        soldier1_currhp = soldier1_currhp - army2_dmg
        soldier2_currhp = soldier2_currhp - army1_dmg
        if (soldier1_currhp <= 0):
            army1_size = army1_size-1
            soldier1_currhp = army1_hp
        if (soldier2_currhp <= 0):
            army2_size = army2_size-1
            soldier2_currhp = army2_hp

        # CHECK FOR WIN CONDITIONS
        if (army1_size <= 0) and (army2_size <= 0):
            print('This war is a DRAW!')
            break
        elif (army1_size <= 0) and (army2_size > 0):
            print('Army 2 is VICTORIOUS!')
            print(army2_soldier*army2_size)
            break
        elif (army2_size > 0) and (army2_size <= 0):
            print('Army 1 is VICTORIOUS!')
            print(army1_soldier*army1_size)
            break

# BATTLE START
input("Press Enter to begin battle!")
battle()
