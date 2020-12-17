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
herostr = random.randint(1,2)
herodef = 0
herol = 1
heroxp = 0

#function for end of game
def end() :

        print("")
        print("                 /                                                                         ")
        print("                |                                                                          ")
        print("               /x\                                                                         ")
        print("              /  x\                                                                        ")
        print("             /_x___\              o o o                                                    ")
        print("                |                _|_|_|_                                                   ")
        print("                |               | _ _ _ |                                                  ")
        print("                |               |_______|                                                  ")
        print("                |                                                                          ")
        print("                |                                                                          ")
        print("                |                                                                          ")
        print("")
        print("Congratulations!!! You've proven your worth and\nfelled the legendary beast known as hexacor.")
        print("Tales of your triumphs are sure to reach the far corners of the land.")
        input("Press enter to return to the village, and never stop growing :)\n")
        system("cls")
        village()

#function for gameover
def gameover() :

        print("Your eyes begin to cloud over, and you start losing a sense of what's around you....")
        input("Game over :( Press enter to return to title.\n")
        system("cls")

        #reroll stats
        global heromhp
        global herostr
        global herodef
        global herol
        global heroxp
        heromhp = random.randint(10,12)
        herostr = random.randint(1,2)
        herodef = 0
        herol = 1
        heroxp = 0

        return heromhp, herostr, herodef, herol, heroxp

#function for tricor enemy
def tricor() :

    #starting hp, enemy stats, global variables
    trichp = 7
    trimhp = 7
    tristr = 1
    tridef = 0
    global heromhp
    global herostr
    global herodef
    global herol
    global heroxp
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
                
                if herostr - tridef < 0 :
                        
                        trichp = trichp
                
                else :
                        
                        trichp = trichp - (herostr - tridef)
                
                if tristr - herodef < 0 :

                        herochp = herochp
                
                else :

                        herochp = herochp - (tristr - herodef)
                
                system("cls")
        
        elif battle == "2" or battle == "run" or battle == "Run" : 

                print("You run away back to the village as quickly as you are able to.")
                input("Press enter to continue.\n")
                system("cls")
                village()
        
        else :

                system("cls")
                print("Please make a valid decision, your life is on the line!")
                

        #enemy defeated
        if trichp <= 0 and herochp > 0 :


                #exp gain, handle level up
                heroxp = heroxp + 3

                if heroxp >= herol * 7 + 5 :

                        print("The tricor crumples in a heap, defeated.\n")
                        print("Congratulations, you leveled up!")
                        
                        herol = herol + 1
                        heromhp = heromhp + random.randint(0,2)
                        herostr = herostr + random.randint(0,2)
                        herodef = herodef + random.randint(0,1)
                        
                        print("Level:",herol,"\nHP:",heromhp,"\nstr:",herostr,"\ndef:",herodef,"\n")
                        input("Press enter to continue back to village.\n")
                        system("cls")
                        return heroxp, heromhp, herostr, herodef

                else :

                        print("The tricor crumples in a heap, defeated.\nYou head back to the village to rest.")
                        input("Press enter to continue.\n")
                        system("cls")
                        return heroxp

        #hero defeated
        if herochp <= 0 :

                trichp = 0
                gameover()

#function for squor enemy
def squor() :

    #starting hp, enemy stats
    sqchp = 15
    sqmhp = 15
    sqstr = 3
    sqdef = 4
    global heromhp
    global herostr
    global herodef
    global herol
    global heroxp
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
                if herostr - sqdef < 0 :
                        
                        sqchp = sqchp
                
                else :
                        
                        sqchp = sqchp - (herostr - sqdef)
                
                if sqstr - herodef < 0 :

                        herochp = herochp
                
                else :

                        herochp = herochp - (sqstr - herodef)
                
                system("cls")
        
        elif battle == "2" or battle == "run" or battle == "Run" : 
                print("You run away back to the village as quickly as you are able to.")
                input("Press enter to continue.\n")
                system("cls")
                village()

        else :

                system("cls")
                print("Please make a valid decision, your life is on the line!")
        
        #enemy defeated
        if sqchp <= 0 and herochp > 0 :

                #exp gain, handle level up
                heroxp = heroxp + 6
                
                if heroxp >= herol * 7 + 5 :

                        print("The squor completely folds over itself, defeated.\n")
                        print("Congratulations, you leveled up!")
                        
                        herol = herol + 1
                        heromhp = heromhp + random.randint(0,2)
                        herostr = herostr + random.randint(0,2)
                        herodef = herodef + random.randint(0,1)
                        
                        print("Level:",herol,"\nHP:",heromhp,"\nstr:",herostr,"\ndef:",herodef,"\n")
                        input("Press enter to continue back to village.\n")
                        system("cls")
                        return heroxp, heromhp, herostr, herodef

                else :

                        print("The squor completely folds over itself, defeated.\nYou head back to the village to rest.")
                        input("Press enter to continue.\n")
                        system("cls")
                        return heroxp

        #hero defeated
        if herochp <= 0 :
               
                sqchp = 0
                gameover()

#function for hexacor phase 2
def hexacor2() :

    #starting hp, enemy stats, global variables
    hex2chp = 50
    hex2mhp = 50
    hex2str = 14
    hex2def = 14
    global heromhp
    global herostr
    global herodef
    herochp = heromhp

    #loop for battle duration
    while hex2chp > 0 :
        
        print("                  Hexacor the Beholden")
        print("                  ___________________ ")
        print("                 /                   \ ")
        print("                /      |       |      \ ")
        print("               /    \      |      /    \ ")
        print("              /      \     |     /      \ ")
        print("             /        \    |    /        \ ")
        print("            /            _   _            \ ")
        print("            \                             / ")
        print("             \        /    |    \        / ")
        print("              \      /     |     \      / ")
        print("               \    /      |      \    / ")
        print("                \      /       \      / ")
        print("                 \___________________/")
        print("                   enemy hp:",hex2chp,"/",hex2mhp)
        print("                   your hp:",herochp,"/",heromhp)
        
        #battle options
        battle = input("1. Attack\n2. Run\n")
        
        if battle == "1" or battle == "attack" or battle == "Attack" :
                
                if herostr - hex2def < 0 :
                        
                        hex2chp = hex2chp
                
                else :
                        
                        hex2chp = hex2chp - (herostr - hex2def)
                
                if hex2str - herodef < 0 :

                        herochp = herochp
                
                else :

                        herochp = herochp - (hex2str - herodef)
                
                system("cls")
        
        elif battle == "2" or battle == "run" or battle == "Run" : 

                system("cls")
                print("You barely have time to flinch in the opposite direction before the newly transformed hexacor blocks your escape.")
        
        else :

                system("cls")
                print("Fight with all you've got!")
                

        #enemy defeated
        if hex2chp <= 0 and herochp > 0 :

                print("The hexacor shatters before you for good this time, time to head home...")
                input("Press enter to continue.\n")
                system("cls")
                end()

        #hero defeated
        if herochp <= 0 :

                hex2chp = 0
                gameover()

#function for hexacor
def hexacor() :

    #starting hp, enemy stats, global variables
    hexchp = 30
    hexmhp = 30
    hexstr = 7
    hexdef = 10
    global heromhp
    global herostr
    global herodef
    herochp = heromhp

    #loop for battle duration
    while hexchp > 0 :
        
        print("                  The mighty Hexacor")
        print("                  __________________ ")
        print("                 /                  \ ")
        print("                /                    \ ")
        print("               /                      \ ")
        print("              /                        \ ")
        print("             /                          \ ")
        print("            /                            \ ")
        print("            \                            / ")
        print("             \                          / ")
        print("              \                        / ")
        print("               \                      / ")
        print("                \                    / ")
        print("                 \__________________/")
        print("                  enemy hp:",hexchp,"/",hexmhp)
        print("                  your hp:",herochp,"/",heromhp)
        
        #battle options
        battle = input("1. Attack\n2. Run\n")
        
        if battle == "1" or battle == "attack" or battle == "Attack" :
                
                if herostr - hexdef < 0 :
                        
                        hexchp = hexchp
                
                else :
                        
                        hexchp = hexchp - (herostr - hexdef)
                
                if hexstr - herodef < 0 :

                        herochp = herochp
                
                else :

                        herochp = herochp - (hexstr - herodef)
                
                system("cls")
        
        elif battle == "2" or battle == "run" or battle == "Run" : 

                system("cls")
                print("The hexacor swiftly moves behind you as you attempt to run, blocking your path of escape.")
        
        else :

                system("cls")
                print("There's no going back now, fight with all you've got!")
                

        #enemy defeated
        if hexchp <= 0 and herochp > 0 :

                print("The mighty hexacor staggers, and just before you believe it's about to fall,\nit starts to tremble, and the cave begins to quake....\n")
                input("Press enter to continue.\n")
                system("cls")
                hexacor2()

        #hero defeated
        if herochp <= 0 :

                hexchp = 0
                gameover()

#function for fields
def fields() :

    system("cls")
    print("                      __                            __              ")
    print("                     \  \                          \  \             ")
    print("                 _______/                      _______/             ")
    print("                                                                    ")
    print("                                                                    ")
    print("                                                                    ")
    print("                                                   / \              ")
    print("                                / \               /___\           / ")
    print("               /        /      /___\                                ")
    print("                                         /                          ")
    print("       /                  /                                /        ")
    print("")
    print("A light breeze drifts through the open fields outside the village.\nIt doesn't take long before you spy a tricor in the distance.")
    input("Press enter to continue.\n")
    system("cls")
    tricor()

#function for mountains
def mountains() :

    system("cls")
    print("                                                                                             ")
    print("                                                                                             ")
    print("                           /\                      /\                /\                      ")
    print("                          /  \       /\           /  \              /  \                     ")
    print("                         /    \     /  \         /    \        /\  /    \                    ")
    print("                 /\     /      \   /    \       /      \      /  \/      \                   ")
    print("          []    /  \   /    [ ] \ /      \     /        \    /    \       \                  ")
    print("          /\   /    \ /     / \  / /\     \   /          \  /      \       \                 ")
    print("         /  \ /      \     /   \/ /  \     \ /            \/     []         \                ")
    print("        /    \        \   /     \/    \     /              \     /\          \               ")
    print("       /               \ /       \     \   /                    /  \          \              ")
    print("")
    print("The wind picks up as you begin ascending the mountains; the climb is not easy.\nAs you climb higher, you begin to notice squor here and there among the lower peaks.\n")
    input("Press enter to continue.\n")
    system("cls")
    squor()

#function for inside cave
def inside() :

        system("cls")
        print("                       ______     ____   __                          _____     __         ")
        print("                    /        / /             |                      /     / /             ")
        print("                   /       /  /               |                   /      / /              ")
        print("    ______    /                                |_____  ______   /                         ")
        print("           /    /                                    /        /                          ")
        print("                                                                                          ")
        print("                                                                                          ")
        print("                                                                                          ")
        print("                                                                                          ")
        print("                                                                                          ")
        print("                                                                                _______   ")
        print("                                                                               /       \  ")
        print("                                                                              /         \ ")
        print("                                                                              \         / ")
        print("    ________________________________ | _______________________________________ \_______/  ")
        print("")
        
        print("As you enter the cave, the bellow of the wind becomes more of a whistle as you leave the entrance behind you.")
        print("Cracks and gaps litter sections of the ceiling, thankfully providing dim light for the otherwise dank cave.")
        print("Eventually, you notice a large figure looming ahead of you.....")
        input("Press enter to continue.\n")
        system("cls")
        hexacor()

#function for cave
def cave() :

        print("                                                                                              ")
        print("               __                              ____                                           ")
        print("             / /  \                           /    \_____                                     ")
        print("            / / | |                      ____/           \_______                             ")
        print("               / /                    __/                        \                            ")
        print("              / /                    /        _______             \                           ")
        print("             / /                    /        /       \             |                          ")
        print("            / /                    /        /         \             \                         ")
        print("                                  |        |           |             |                        ")
        print("                                  |        |           |              |                       ")
        print("                    |            /         |           |               |                      ")
        print("                    |                                                   |                     ")
        print("                    |                                                                         ")
        print("                                                                                              ")
        print("")
        print("You decide to explore even higher into the mountaintops.\nThe wind pierces through your skin as you near the top, and a chill frost glazes the ground beneath your feet.\n")
        print("As you approach the summit, you locate the cave said to house a vicious creature....")

        #final chance to leave before final boss
        final = input("Taking a moment to think, you realize there may be no returning once you enter, are you sure you want to head in?\n1. Yes\n2. No\n")

        if final == "1" or final == "yes" or final == "Yes" :

                inside()
        
        elif final == "2" or final == "no" or final == "No" :

                print("Maybe another day....")
                input("Press enter to return to village.\n")
                system("cls")
                village()

        else :

                system("cls")
                print("It's kinda cold up here, you should probably decide soon.")
                cave()

#function to check stats
def stats() :

        system("cls")
        print("Level:",herol,"\nHP:",heromhp,"\nstr:",herostr,"\ndef:",herodef,"\ncurrent exp:",heroxp,"\nexp to level:",herol * 7 + 5)
        input("Press enter to continue.\n")
        system("cls")
        village()

#function for village
def village() :

    print("The village is quiet, as usual.")

    #choices of where to go
    map = input("1. Fields\n2. Mountains\n3. Cave at summit\n4. Stats\n")

    if map == "1" or map == "fields" or map == "Fields" :

            fields()

    elif map == "2" or map == "mountains" or map == "Mountains" :

            mountains()

    elif map == "3" or map == "cave at summit" or map == "Cave at summit" or map == "cave" or map == "Cave":

            system("cls")
            cave()

    elif map == "4" or map == "stats" or map == "Stats" :

            stats()
    
    else :
        
        system("cls")
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
        input("Press enter to begin\n")

        
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

        system("cls")
        village()

#start
while True :

        while heroxp == 0 :

                title()

        while heroxp > 0 :

                village()

