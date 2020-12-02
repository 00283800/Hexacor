#Matt Webster
#Programming for IT CIS-153
#Final Project
#Hexacor, text-based role playing game

#allows import of system command to clear screen from python
from os import system

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

#start game
print("")
print("")
input("Press enter to begin")

#clear title after beginning
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
hname = input("Now...what is your name?\n")
input()