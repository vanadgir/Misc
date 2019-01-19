import os
from random import choice
import random

# TITLE
os.system('clear')
print("|---------------------------------|")
print("|-----------THE DINDLER-----------|")
print("|---------------------------------|")

# INITALIZE LISTS
races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling','Half-Orc', 'Human', 'Tiefling']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk','Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

backgrounds = ['Acolyte', 'Charlatan', 'Criminal/Spy', 'Entertainer','Folk Hero', 'Gladiator', 'Guild Artisan/Guild Merchant', 'Hermit', 'Knight', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Urchin']

#savedDict = {}

def stat_roll():
    roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll = int(sum(sorted(roll)[1:]))
    return roll

#def save_dindle(char, stat_points):
    #savedDict = {'race':str(char[0]), 'class':str(char[1]), 'background':str(char[2]),
    #    'stat1':stat_points[0], 'stat2':stat_points[1], 'stat3':stat_points[2],
    #    'stat4':stat_points[3], 'stat5':stat_points[4], 'stat6':stat_points[5]}
    #print('Dindle Saved.')

#def load_dindle():
    #os.system('clear')
    #print(savedDict)
    #print('|---------------------------------')
    #print('| Hello!                          ')
    #print('| Nice to meet you! I am:         ')
    #print('|---------------------------------')
    #print('| RACE:   ' + str(char[0]) + '    ')
    #print('| CLASS:  ' + str(char[1]) + '    ')
    #print('| B/G:    ' + str(char[2]) + '    ')
    #print('|---------------------------------')
    #print('| My available stats are:         ')
    #print('| '+str(stat_points[0])+', '+str(stat_points[1])+', '+str(stat_points[2])+', '+str(stat_points[3])+', '+str(stat_points[4])+', '+str(stat_points[5]))
    #print('|---------------------------------')

def random_char():
    char = [choice(races),choice(classes),choice(backgrounds)]
    stat_points = [stat_roll(), stat_roll(), stat_roll(),stat_roll(), stat_roll(), stat_roll()]

    os.system('clear')
    print('|---------------------------------')
    print('| Hello!                          ')
    print('| Nice to meet you! I am:         ')
    print('|---------------------------------')
    print('| RACE:   ' + str(char[0]) + '    ')
    print('| CLASS:  ' + str(char[1]) + '    ')
    print('| B/G:    ' + str(char[2]) + '    ')
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
        print("Thanks for Dindlin'!")

input('Press Enter to get a random DnD character!')
random_char()
