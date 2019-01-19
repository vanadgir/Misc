import os
from random import choice
import random
import pandas as pd

# TITLE
os.system('clear')
print("|---------------------------------|")
print("|-----------THE DINDLER-----------|")
print("|---------------------------------|")

# INITALIZE LISTS
races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling','Half-Orc', 'Human', 'Tiefling']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk','Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

backgrounds = ['Acolyte', 'Charlatan', 'Criminal/Spy', 'Entertainer','Folk Hero', 'Gladiator', 'Guild Artisan/Guild Merchant', 'Hermit', 'Knight', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Urchin']

# rolls 4 dice, drops lowest, gets sum
def stat_roll():
    roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll = int(sum(sorted(roll)[1:]))
    return roll

dindl_history = []

# generate random character
def random_char():
    # choose race, class, background, and roll for 6 stat points
    char = [choice(races),choice(classes),choice(backgrounds)]
    stat_points = [stat_roll(), stat_roll(), stat_roll(),stat_roll(), stat_roll(), stat_roll()]

    colnames = ['race', 'class', 'background', 'stat1', 'stat2', 'stat3', 'stat4', 'stat5', 'stat6']

    char_stats = [char[0], char[1], char[2], stat_points[0], stat_points[1], stat_points[2], stat_points[3], stat_points[4], stat_points[5]]

    dindl_history.append(char_stats)

    # print the character profile
    os.system('clear')
    print('|---------------------------------')
    print('| Hello!                          ')
    print('| Nice to meet you! I am:         ')
    print('|---------------------------------')
    print('| RACE:   ' + char[0] + '    ')
    print('| CLASS:  ' + char[1] + '    ')
    print('| B/G:    ' + char[2] + '    ')
    print('|---------------------------------')
    print('| My available stats are:         ')
    print('| ' + str(stat_points[0]) + ', ' + str(stat_points[1]) + ', ' + str(stat_points[2]) + ', ' + str(stat_points[3]) + ', ' + str(stat_points[4]) + ', ' + str(stat_points[5]))
    print('|---------------------------------')
    print('| How would you like to proceed?  ')
    howToProceed = input("| 'd' to Dindle again. 'x' to Exit.\n")
    while (howToProceed!='d') and (howToProceed!='x'):
        print('| Please enter a valid action.')
        howToProceed = input("| 'd' to Dindle again. 'x' to Exit.\n")
    if (howToProceed=='d'):
        random_char()
    elif (howToProceed=='x'):
        df = pd.DataFrame(dindl_history, columns=colnames)
        df.to_csv('dindl.csv')
        print("Thanks for Dindlin'!")

# BEGINNING OF DINDLER
input('Press Enter to get a random DnD character!')
random_char()
