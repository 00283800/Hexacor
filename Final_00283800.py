#Matt Webster
#Programming for IT CIS-153
#Final Project
#Hexacor, text-based role playing game

#allows import of system command to clear screen from python
from os import system

#imports random function
import random

#stats will be randomized at the start of the program
heromhp = random.randint(10,12)

#function for gameover
def gameover() :
        print("Your eyes begin to cloud over, and you start losing a sense of what's around you....")
        input("Game over :( Press enter to return to title.\n")
        system("cls")
        title()

#function for tricor enemy
def tricor() :

    #starting hp, enemy stats
    trichp = 7
    trimhp = 7
    herochp = heromhp

    #loop for battle duration
    while trichp > 0 :
        
        print("             /\ ")
        print("            /  \ ")
        print("           /    \ ")
        print("          /      \ ")
        print("         /        \ ")
        print("        /__________\ ")
        print("     enemy hp:",trichp,"/",trimhp)
        print("     your hp:",herochp,"/",heromhp)
        
        #battle options
        battle = input("1. Attack\n2. Run\n")
        
        if battle == "1" or battle == "attack" or battle == "Attack" :
                trichp = trichp - 1
                herochp = herochp - 1
        
        elif battle == "2" or battle == "run" or battle == "Run" : 
                print("You run away back to the village as quickly as you are able to.")
                input("Press enter to continue.\n")
                system("cls")
                village()
        
        else :
                print("Please make a valid decision, your life is on the line!")

        #enemy defeated
        if trichp <= 0 and herochp > 0 :
                print("The tricor crumples in a heap, defeated.\nYou head back to the village to rest.")
                input("Press enter to continue.\n")
                system("cls")
                village()

        #hero defeated
        if herochp <= 0 :

                trichp = 0
                gameover()

#function for squor enemy
def squor() :

    #starting hp, enemy stats
    sqchp = 15
    sqmhp = 15
    herochp = heromhp

    #loop for battle duration
    while sqchp > 0 :
        
        print("         ________________  ")
        print("        |                | ")
        print("        |                | ")
        print("        |                | ")
        print("        |                | ")
        print("        |                | ")
        print("        |                | ")
        print("        |                | ")
        print("        |________________| ")
        print("        enemy hp:",sqchp,"/",sqmhp)
        print("        your hp:",herochp,"/",heromhp)

        #battle options
        battle = input("1. Attack\n2. Run\n")
        
        if battle == "1" or battle == "attack" or battle == "Attack" :
                sqchp = sqchp - 1
                herochp = herochp - 1
        
        elif battle == "2" or battle == "run" or battle == "Run" : 
                print("You run away back to the village as quickly as you are able to.")
                input("Press enter to continue.\n")
                system("cls")
                village()

        else :
                print("Please make a valid decision, your life is on the line!")
        
        #enemy defeated
        if sqchp <= 0 and herochp > 0 :
                print("The squor completely folds over itself, defeated.\nYou head back to the village to rest.")
                input("Press enter to continue.\n")
                system("cls")
                village()

        #hero defeated
        if herochp <= 0 :
               
                sqchp = 0
                gameover()

#function for fields
def fields() :

    system("cls")
    print("A light breeze drifts through the open fields outside the village.\nIt doesn't take long before you spy a tricor in the distance.")
    print("                                                                                                             /_\ ")
    input("Press enter to continue.\n")
    system("cls")
    tricor()

#function for mountains
def mountains() :

    system("cls")
    print("The wind picks up as you begin ascending the mountains; the climb is not easy.\nAs you climb higher, you begin to notice squor here and there among the peaks.\n")
    print("                                                []            []                [] ")
    input("Press enter to continue.\n")
    system("cls")
    squor()

#function for village
def village() :

    print("The village is quiet, as usual.")

    #choices of where to go
    map = input("1. Fields\n2. Mountains\n3. Cave at summit\n")
    if map == "1" or map == "fields" or map == "Fields" :
            fields()

    elif map == "2" or map == "mountains" or map == "Mountains" :
            mountains()

    elif map == "3" or map == "cave at summit" or map == "Cave at summit" :
            print("cave at summit")
            village()

    else :
        print("Please submit a valid choice.")
        village()

#function for title
def title() :

        #title
        print(" ____        ____     ________________    ____                  ____            ______                  _______________      ________________      __________________ ")
        print("|    |      |    |   |                |   \    \               /   /           |      |                /               |    |                |    |                  \ ")
        print("|    |      |    |   |                |    \    \             /   /            |      |               /                |    |                |    |     ________      \ ")
        print("|    |      |    |   |      __________|     \    \           /   /            |        |             /        _________|    |                |    |    |        \      \ ")
        print("|    |      |    |   |     |                 \    \         /   /             |   __   |            /        /              |     ______     |    |    |         \      | ")
        print("|    |      |    |   |     |                  \    \       /   /             |   |  |   |          |        /               |    |      |    |    |    |          |     | ")
        print("|    |      |    |   |     |                   \    \     /   /              |   |  |   |         |        /                |    |      |    |    |    |         /     | ")
        print("|    |______|    |   |     |__________          \    \   /   /              |   |    |  |        |        /                 |    |      |    |    |    |________/     | ")
        print("|                |   |                |          \    \_/   /              |    |____|   |      |        /                  |    |  __  |    |    |                  | ")
        print("|                |   |                |           |    _    |              |             |      |       |                   |    | /  \ |    |    |      ________     \ ")
        print("|     ______     |   |      __________|          /    / \    \             |    _____    |      |        \                  |    | \__/ |    |    |     |        \     \ ")
        print("|    |      |    |   |     |                    /    /   \    \           |    |     |    |      |        \                 |    |      |    |    |     |         \     \ ")
        print("|    |      |    |   |     |                   /    /     \    \          |    |     |    |       |        \                |    |      |    |    |     |          \     \ ")
        print("|    |      |    |   |     |                  /    /       \    \        |    |       |    |       |        \               |    |______|    |    |     |           \     \ ")
        print("|    |      |    |   |     |__________       /    /         \    \       |    |       |    |        \        \_________     |                |    |     |            \     \ ")
        print("|    |      |    |   |                |     /    /           \    \     |    |         |    |        \                 |    |                |    |     |             \     \ ")
        print("|    |      |    |   |                |    /    /             \    \    |    |         |    |         \                |    |                |    |     |              \     \ ")
        print("|____|      |____|   |________________|   /____/               \____\   |____|         |____|          \_______________|    |________________|    |_____|               \_____\ ")

        print("")
        print("")
        input("Press enter to begin")

        
        system("cls")

        #intro
        print("")
        print("")
        print("                  |")
        print("                  |")
        print("                  |")
        print("                  |")
        print("                  |")
        print("                  |")
        print("")
        print("")
        print("You are but a single line in a land full of shapes.\nSome day you hope to prove yourself and show that you're not just another one-dimensional being....")
        input("Press enter to continue....\n")

        system("cls")
        print("Hey...you...\n  Hey...wake up..!\n\nYou awake from a deep sleep, groggy but ready to start the day.")
        input("Press enter to continue.\n")

        village()

#start
title()
