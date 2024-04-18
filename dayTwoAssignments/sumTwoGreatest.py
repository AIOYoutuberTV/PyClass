from numpy import sort


treasure = [int(input()),int(input()),int(input())]
treasureVetted = sort(treasure)

print(treasureVetted[1] + treasureVetted[2])