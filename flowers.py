flowerCount = int(input("Number of flowers (n): "))
daysSim = int(input("Amount of days (k): "))

i = 1 #initialise counter
while True:
    if i <= daysSim: #Check if simulation is complete
        i += 1 #Increment
        flowerCount *= 3 #Multiply the flowers
    else: #Condition: Simulation complete
        break

print("Total flowers = ",flowerCount)